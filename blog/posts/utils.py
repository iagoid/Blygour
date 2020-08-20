from django.core.paginator import Paginator
from django.contrib import messages
from django.shortcuts import redirect

import hashlib
import string
import random

def random_key(size=5):
    chars =string.ascii_uppercase + string.digits
    return ''.join(random.choice(chars) for x in range(size))

def generate_hash_key(salt, random_str_size=5):
    random_str = random_key(random_str_size)
    text = random_str + salt
    return hashlib.sha224(text.encode('utf-8')).hexdigest()


"""
Utilizações nas views
"""
def pagination(request, posts_list):

    paginator = Paginator(posts_list, 7)
    page = request.GET.get('page')
    return paginator.get_page(page)