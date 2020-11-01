import os

# TODO: Verificar real necessidade desta variavel aqui
ENVIRONMENT = os.getenv('ENVIRONMENT', 'development')


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# '-05sgp9!deq=q1nltm@^^2cc+v29i(tyybv3v2t77qi66czazj'

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'dashboard.apps.DashboardConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
]

# my installed apps
MY_APPS = [
    'core.apps.CoreConfig',
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
    'contasdeusuario.apps.ContasdeusuarioConfig',
    'batalhao.apps.BatalhaoConfig',
    'rat.apps.RatConfig',
    'pessoa.apps.PessoaConfig',
    'anexo.apps.AnexoConfig',
    'opo.apps.OpoConfig'
]

EXTERNAL_LIBRARYS = [
    'rest_framework',  # rest framework
    'rest_framework.authtoken',  # autenticação do django rest framework
]

INSTALLED_APPS += MY_APPS
INSTALLED_APPS += EXTERNAL_LIBRARYS

X_FRAME_OPTIONS = 'ALLOWALL'

XS_SHARING_ALLOWED_METHODS = ['POST', 'GET', 'OPTIONS', 'PUT', 'DELETE']

AUTH_USER_MODEL = 'contasdeusuario.Usuario'  # policial como usuario

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 10
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware'
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

# START CORS CONFIG
# CORS_ORIGIN_ALLOW_ALL = True

CORS_ORIGIN_WHITELIST = [
    'http://localhost:8000',
    'http://rop-e.com',
    'http://ropd.tk',
    'http://localhost',
]


CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]

CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]
# END-OF CORS CONFIG

if os.environ.get('DATABASE') == 'MYSQL':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.environ.get('DB_NAME'),
            'USER': os.environ.get('DB_USER'),
            'PASSWORD': os.environ.get('DB_PASSWORD'),
            'HOST': os.environ.get('DB_HOST'),
            'PORT': os.environ.get('DB_PORT'),
        }
    }
elif os.environ.get('DATABASE') == 'POSTGRESQL':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.environ.get('DB_NAME'),
            'USER': os.environ.get('DB_USER'),
            'PASSWORD': os.environ.get('DB_PASSWORD'),
            'HOST': os.environ.get('DB_HOST'),
            'PORT': os.environ.get('DB_PORT'),
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(BASE_DIR, 'db.sqlite3')
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
TIME_ZONE = 'America/Bahia'
USE_I18N = True
USE_L10N = True
USE_TZ = True

LOGIN_URL = '/contas/entrar/'  # URL para login

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static_files')]

# TODO: Verificar se realmente necessita desta variavel
#STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
PDF_ROOT = MEDIA_ROOT + '/pdf/'  # Path pdf url

ENVIRONMENT = os.environ.get('ENVIRONMENT')

if ENVIRONMENT == 'production':
    DEBUG = os.environ.get('DEBUG')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    # SESSION_COOKIE_SECURE = True
    # SECURE_BROWSER_XSS_FILTER = True
    # SECURE_CONTENT_TYPE_NOSNIFF = True
    # SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    # SECURE_HSTS_SECONDS = 31536000
    # SECURE_REDIRECT_EXEMPT = []
    # SECURE_SSL_REDIRECT = True
    # SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
else:
    DEBUG = True
    SECRET_KEY = '123456789)*(&^%$#@'
