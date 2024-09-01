import json
from pathlib import Path

from django.core.management.base import BaseCommand, CommandError

from product.management.creators import AttributesCreator

CREATOR_MAP = {
    "attributes": AttributesCreator,
}


class Command(BaseCommand):
    help = "Choose and run a creator to set data related to a specific model"

    def add_arguments(self, parser):
        parser.add_argument(
            "file_path_or_name",
            type=str,
            help="An absolute or relative path to the JSON file containing attributes data ",
        )
        parser.add_argument(
            "creator_type",
            type=str,
            choices=CREATOR_MAP.keys(),
            help="The type of creator to use (must be one of: {})".format(", ".join(CREATOR_MAP.keys())),
        )

    def handle(self, *args, **options):
        self.file_path = Path(options["file_path_or_name"])
        self.data = self.get_json_data()
        creator_class = CREATOR_MAP[options["creator_type"]]
        creator = creator_class(data=self.data, command_obj=self)
        creator.create()
        
    def get_json_data(self):
        self.validate_file_path()

        with self.file_path.open() as f:
            data = json.load(f)
        
        return data

    def validate_file_path(self):
        """
        Check if the file exists and is a JSON file
        """
        if not self.file_path.exists():
            msg = f"File not found: {self.file_path}"
            raise CommandError(msg)

        if self.file_path.suffix != ".json":
            raise CommandError("File must be a JSON file")
