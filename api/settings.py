import os
import datetime
"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 3.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'i@@b#=^2c-k9*9++e0z(ss!-!^o)qt1fqcp#0ip)b)-=r5lfg5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', '.herokuapp.com']

CORS_ORIGIN_WHITELIST = ['http://localhost:3000'] #아까 설치한 corsheaders로 해당 서버와 연결할 서버의 url을 작성해준모습

# Application definition
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'oauth',
    'rest_framework', 
    'dashboard',
    'corsheaders', 
]



MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',     # 추가
    'django.middleware.common.CommonMiddleware', # 추가
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'api.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'api.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'djangogirls',
        'USER': 'name',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
    }
}

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static/")

# AUTH_USER_MODEL = 'jandis.User'

REST_FRAMEWORK = { # 추가
    'DEFAULT_PERMISSION_CLASSES': [
        # 'rest_framework.permissions.IsAuthenticated',  #인증된 회원만 액세스 허용
        # 'rest_framework.permissions.AllowAny',         #모든 회원 액세스 허용
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': ( #api가 실행됬을 때 인증할 클래스를 정의해주는데 우리는 JWT를 쓰기로 했으니
        # 'rest_framework_jwt.authentication.JSONWebTokenAuthentication', #이와 같이 추가해준 모습이다.
        # 'rest_framework.authentication.SessionAuthentication',
        # 'rest_framework.authentication.BasicAuthentication',
    ),
}

# JWT_AUTH = { # 추가
#    'JWT_SECRET_KEY': SECRET_KEY,
#    'JWT_ALGORITHM': 'HS256',
#    'JWT_VERIFY_EXPIRATION' : True, #토큰검증
#    'JWT_ALLOW_REFRESH': True, #유효기간이 지나면 새로운 토큰반환의 refresh
#    'JWT_EXPIRATION_DELTA': datetime.timedelta(minutes=30),  # Access Token의 만료 시간
#    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=3), # Refresh Token의 만료 시간
#    'JWT_RESPONSE_PAYLOAD_HANDLER': 'api.custom_responses.my_jwt_response_handler'
# }


CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

CORS_ORIGIN_WHITELIST = ['http://127.0.0.1:3000' ,'http://localhost:3000'] 

