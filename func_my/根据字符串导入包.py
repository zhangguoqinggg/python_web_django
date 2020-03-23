import importlib
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'python_web_django.settings')
    s = ''
    ret1 = s.rsplit('.')
    module_obj = importlib.import_module(ret1[0])
    if hasattr(module_obj,ret1[1]):
        class_obj = getattr(module_obj,ret1[1])
        print(class_obj)
