"""
Django settings for taskmanagement project.

Generated by 'django-admin startproject' using Django 4.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path

SECRET_KEY = 'fastapi-insecure--_t)&hwjzixaj$$83hve-$ck0ab=#ohre4_5@$g7d=#39@egwo'



# SECURITY WARNING: don't run with debug turned on in production!
# JWT settings
JWT_TOKEN_EXPIRY = 7   # No. of days
JWT_ALGORITHM = 'HS256'  # Algorithm specified by JWT
JWT_UTF = 'utf-8'

