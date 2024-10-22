
import re

from django.core.exceptions import ValidationError


YEAR_RANGE = (1999, 2030)


def alphabet_validator(name):
    if not re.match(r'^[A-Za-z0-9_]+$', name):
        raise ValidationError("Username must contain only letters, digits, and underscores!")


def year_validator(year):
    if year not in range(YEAR_RANGE[0], YEAR_RANGE[1]):
        raise ValidationError("Year must be between 1999 and 2030!")
