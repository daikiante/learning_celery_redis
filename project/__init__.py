"""
Django 起動時にcelery.pyからappをインポートしてロードする
"""

from .celery import app as celery_app

__all__ = ('celery_app', )