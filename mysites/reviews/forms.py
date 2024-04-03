from .models import Reviewer
from django.forms import Form, ModelForm, ValidationError
from django import forms
from django.core import validators
from django.core.validators import validate_email
# from django.db.models import CharField, EmailField # not the same with forms.CharField


class ReviewerForm(ModelForm):

    class Meta:
        model = Reviewer
        # fields = ["first_name", "last_name", "reviewer_email"]
        fields = "__all__"
        # excluded fields don't get validation
        exclude = []

    # custom validation here methods if the validator of my fields
    # do not satisfy me, add get_cleaned_something in the validation method here,
    # to get cleaned data first then process it more


class CustomReviewerForm(Form):
    first_name = forms.CharField(label="your first name", max_length=40)
    last_name = forms.CharField(
        label="your last name", max_length=40, widget=forms.Textarea,
        help_text="Votre Prénom", required=False, validators=[validate_email,validators.EmailValidator])
    #  beware silly validator bug in your validators list
    reviewer_email = forms.CharField(
        label="email", max_length=40)  # in django.forms.required=True by default

# validation examples
"""
class ContactForm(forms.Form):
    # Everything as before.
    ...

    def clean(self):
        # super().clean()
        cleaned_data = super().clean()
        cc_myself = cleaned_data.get("cc_myself")
        subject = cleaned_data.get("subject")

        if cc_myself and subject:
            # Only do something if both fields are valid so far.
            if "help" not in subject:
                raise ValidationError(
                    "Did not send for 'help' in the subject despite " "CC'ing yourself."
                )
"""
# cleaning specific fields
"""
from django import forms
from django.core.exceptions import ValidationError


class ContactForm(forms.Form):
    # Everything as before.
    ...

    def clean_recipients(self):
        data = self.cleaned_data["recipients"]
        if "fred@example.com" not in data:
            raise ValidationError("You have forgotten about Fred!")

        # Always return a value to use as the new cleaned data, even if
        # this method didn't change it.
        return data
    def clean(self):
        self.recipients=self.clean_recipients()
        ...
"""
# cleaning a form entirely and easily, ovveride validate
"""
from django import forms
from django.core.validators import validate_email


class MultiEmailField(forms.Field):
    def to_python(self, value):
        # Normalize data to a list of strings.
        # Return an empty list if no input was given.
        if not value:
            return []
        return value.split(",")

    def validate(self, value):
        # Check if value consists only of valid emails.
        # Use the parent's handling of required fields, etc.
        super().validate(value)
        for email in value:
            validate_email(email)
"""
# creating validators for fields
"""
from django.core import validators
from django.forms import CharField

class SlugField(CharField):
    default_validators = [validators.validate_slug]

As you can see, SlugField is a CharField with a customized validator
that validates that submitted text obeys to some character rules.
This can also be done on field definition so:
slug = forms.SlugField()
is equivalent to:
slug = forms.CharField(validators=[validators.validate_slug])
"""
"""
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(
            _("%(value)s is not an even number"),
            params={"value": value},
        )

You can add this to a model field via the field’s validators argument:
from django.db import models
class MyModel(models.Model):
    even_field = models.IntegerField(validators=[validate_even])

Because values are converted to Python before validators are run,
you can even use the same validator with forms:

from django import forms
class MyForm(forms.Form):
    even_field = forms.IntegerField(validators=[validate_even])
"""
class SillyForm(forms.Form):
    pass

