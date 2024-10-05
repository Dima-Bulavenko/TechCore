from typing import Callable

from django.http import HttpRequest, HttpResponse
from django.template.loader import render_to_string


class HTMXCartMiddleware:

    def __init__(self, get_response: Callable[[HttpRequest], HttpResponse]):
        self._get_response = get_response

    def __call__(self, request: HttpRequest) -> HttpResponse:
        """Middleware implementation"""

        response = self._get_response(request)

        if request.htmx:    
            response.write(
                render_to_string(
                    template_name="components/shopping_card_button.html",
                    context={"hx_oob": True},
                    request=request
                )
            )
        
        return response
            
