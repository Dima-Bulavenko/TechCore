from django import template

register = template.Library()


@register.inclusion_tag('product/inclusions/rating_stars.html')
def render_stars(rating):
    rating = float(rating)
    max_rating = 5
    fill_sizes = []
    for i in range(max_rating):
        fill_size = 0
        full_star_check = rating - i
        if full_star_check >= 1:
            fill_size = 100
        elif full_star_check > 0:
            fill_size = full_star_check * 100
        fill_sizes.append(fill_size)
    return {'fill_sizes': fill_sizes}