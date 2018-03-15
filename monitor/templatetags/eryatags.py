# -*- encoding=utf-8 -*-
from django import template 

register = template.Library()

from util.cryption import Cryption

@register.filter(name='encrypt')
def encrypt(value):
    if isinstance(value, long) or isinstance(value, int):
        value = str(value)
    return Cryption.encrypt(value)
