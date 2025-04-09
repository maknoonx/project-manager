# project_manager/wsgi.py
import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_manager.settings')

application = get_wsgi_application()
application = WhiteNoise(application)