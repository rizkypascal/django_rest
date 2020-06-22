from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _
import re

# Create your models here.
class Users(models.Model):
    name = models.TextField(max_length=50)
    phone = models.TextField(max_length=50)

    def clean(self):
        error_dict = {}
        if self.name is None:
            error_dict['name'] = ValidationError(_('Name should be filled'))
        elif self.name is not None and any(char.isdigit() for char in self.name):
            error_dict['name'] = ValidationError(_('Name should not contain numbers'))
        elif self.phone is None:
            error_dict['phone'] = ValidationError(_('Phone should be filled'))
        elif self.phone is not None and self.phone.match(re.compile("(\+62 ((\d{3}([ -]\d{3,})([- ]\d{4,})?)|(\d+)))|(\(\d+\) \d+)|\d{3}( \d+)+|(\d+[ -]\d+)|\d+")):
            error_dict['phone'] = ValidationError(_('Phone format should +62xxxxxx or 08xxxxxx'))

        if bool(error_dict):
            raise ValidationError(error_dict)