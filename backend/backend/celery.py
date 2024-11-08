import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

celery_app = Celery('backend')

celery_app.config_from_object('django.conf:settings', namespace='CELERY')

celery_app.autodiscover_tasks()


'''
init.py in backend


from .celery import celery_app

__all__ = ('celery_app',)


settings.py same folder


CELERY_BROKER_URL = 'redis://localhost:6379/0'


celery -A backend worker -E -l info run from backend where settings is.

-E allow events to be monitored
-l logging
'''