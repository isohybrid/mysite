from django.conf.urls.defaults import *
from registration.views import register

from tstcaptcha.forms import RecaptchaRegistrationForm

urlpatterns = patterns('',
    url(r'register/$', register,
      {'form_class': RecaptchaRegistrationForm, 'backend': 'registration.backends.default.DefaultBackend'},
      name='registration.views.register'),
    (r'^$', include('registration.urls')),
)
