import os
import sys

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'python_web_django.settings')

    import django
    django.setup()

    from  app01.models import Publisher
    obj_pubblisher = Publisher.objects.first()
    print( obj_pubblisher.name)