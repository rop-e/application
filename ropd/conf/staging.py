import os
import django_heroku

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'brz@!a-2iahqywx355l$!zs#=s)@3$!sdzw!2njcp!3uvpr94@'

DEBUG = True

ALLOWED_HOSTS = []

print(os.environ['DATABASE_NAME'])

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles'
]

MY_APPS = [
    'viatura.apps.ViaturaConfig',
    'guarnicao.apps.GuarnicaoConfig',
    'ocorrencia.apps.OcorrenciaConfig',
    'policial.apps.PolicialConfig',
    'policialviatura.apps.PolicialviaturaConfig',
    'observacao.apps.ObservacaoConfig',
    'envolvido.apps.EnvolvidoConfig',
    'localrecebedor.apps.LocalrecebedorConfig',
    'endereco.apps.EnderecoConfig',
    'procedimentoocorrencia.apps.ProcedimentoocorrenciaConfig',
    'acessoriosocorrencia.apps.AcessoriosocorrenciaConfig',
    'veiculo.apps.VeiculoConfig',
    'contasdeusuario.apps.ContasdeusuarioConfig'
]

EXTERNAL_LIBRARYS = [
    'rest_framework',  # rest framework
    'rest_framework.authtoken',  # autenticação do django rest framework
]

AUTH_USER_MODEL = 'contasdeusuario.Usuario'  # policial como usuario

INSTALLED_APPS += MY_APPS
INSTALLED_APPS += EXTERNAL_LIBRARYS

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ]
}  # autenticação do django rest framework

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ropd.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates/')],
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

WSGI_APPLICATION = 'ropd.wsgi.application'

DATABASES = {
    'default': {
        'NAME': os.environ['DATABASE_NAME'],
        'ENGINE': 'django.db.backends.postgresql',
        'USER': os.environ['DATABASE_USER'],
        'PASSWORD': os.environ['DATABASE_PASSWORD'],
        'HOST': os.environ['DATABASE_HOST'],
        'PORT': int(os.environ['DATABASE_PORT']),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME':
        'django.contrib.auth.password_validation.'  # linha alterada
        'UserAttributeSimilarityValidator',  # linha alterada
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
STATIC_URL = '/static/'

LOGIN_URL = 'contas/entrar/'

# Activate Django-Heroku.
django_heroku.settings(locals())
