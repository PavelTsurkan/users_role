import os
import django


os.environ.setdefault(key="DJANGO_SETTINGS_MODULE", value="user_role.settings")
django.setup()