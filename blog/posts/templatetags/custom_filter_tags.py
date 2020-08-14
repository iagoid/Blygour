from django import template

register = template.Library()

@register.simple_tag(name="check_profile_picture_exists")
def check_profile_picture(url_img):
    if(url_img):
        return url_img.url
    else:
        return '/media/static/avatar.png'

