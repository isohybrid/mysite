from django import forms
import fields as brecaptcha_fields
from registration.forms import RegistrationForm

class RecaptchaRegistrationForm(RegistrationForm):
  recaptcha = brecaptcha_fields.ReCaptchaField()
