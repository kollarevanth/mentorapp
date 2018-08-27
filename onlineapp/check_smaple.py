import os,django
os.environ.setdefault('DJANGO_SETTINGS_MODULE',"online.settings")
django.setup()

from onlineapp.models import *

manager=College.objects
query_sets=College.objects.all()
print(query_sets)
for query_set in query_sets:
    print(query_set)