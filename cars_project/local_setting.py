# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-z7g&dl^01=%x7o3*j0tm7q#r&sepwfbv)p0514q^e7j#8vc+fi'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cars_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'Password',
    }
}