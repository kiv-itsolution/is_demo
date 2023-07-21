# Пример local_settings
# Измените данные на свои

DEBUG = True
ALLOWED_HOSTS = ['*']

from integration_utils.bitrix24.local_settings_class import LocalSettingsClass


TINKOFF_API_KEY = 'OcxkrOFzdALb7WubboufleAyhLc7MS3y'
ENDPOINT = 'api.tinkoff.ai:443'
API_KEY = 'H59znTW1kDdUUzr3wb98dm6hxTrcogtMQ13gP1D9lts='
SECRET_KEY = 'rcjUgeuMRidw9U/GSRr1JZGdIuEwoJRdpePteUTu4Cw='

APP_SETTINGS = LocalSettingsClass(
    portal_domain='is-demo.bitrix24.ru',
    app_domain='127.0.0.1:8000',
    app_name='is-demo',
    salt='wefiewofioiI(IF(Eufrew8fju8ewfjhwkefjlewfjlJFKjewubhybfwybgybHBGYBGF',
    secret_key='wefewfkji4834gudrj.kjh237tgofhfjekewf.kjewkfjeiwfjeiwjfijewf',
    application_bitrix_client_id='local.5f3e7d07b03783.01669857',
    application_bitrix_client_secret='VjIgCTk8PccYnJ4I25hJb1vdoVfncvQh4gmeZEHXZPE3rm5eGc',
    application_index_path='/',
)



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'is_demo',  # Or path to database file if using sqlite3.
        'USER': 'is_demo',  # Not used with sqlite3.
        'PASSWORD': 'password',  # Not used with sqlite3.
        'HOST': 'localhost',
    },
}