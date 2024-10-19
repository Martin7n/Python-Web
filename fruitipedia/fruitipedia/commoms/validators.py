from django.core.exceptions import ValidationError


def first_letter_validator(name):
    if not name[0].isalpha():
        raise ValidationError('Your name must start with a letter!')

def only_letters(name):
    if not name.isalpha():
        raise ValidationError('Fruit name should contain only letters!')