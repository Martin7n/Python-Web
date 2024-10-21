
import re

from django.core.exceptions import ValidationError


def alphabet_validator(name):
    if not re.match(r'^[A-Za-z0-9_]+$', name):
        raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")
