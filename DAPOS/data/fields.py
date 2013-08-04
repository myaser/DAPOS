import re
from django.utils import simplejson as json
from django.db import models


class RegexPatternField(models.TextField):
    __metaclass__ = models.SubfieldBase
    description = "regex pattern"

    def to_python(self, value):
        """
        Converting database string to Python compiled Regex pattern
        """
        if not value:
            value = re.compile('')

        # TODO: Validation and raise FieldError when not valid

        return re.compile(value)

    def get_prep_value(self, value):
        """
        Converting Python compiled Regex pattern to database string
        """
        if type(value) == type(re.compile('')):
            return value.pattern
        else:
            raise TypeError("RegexPatternField can't accept"
                            "{type} entries".format(type=type(value)))

    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return self.get_prep_value(value)


class ListField(models.TextField):
    __metaclass__ = models.SubfieldBase
    description = "Stores a python list"

    def __init__(self, *args, **kwargs):
        super(ListField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        if not value:
            value = []

        if isinstance(value, list):
            return value

        return json.loads(value, use_decimal=True)

    def get_prep_value(self, value):
        if value is None:
            return value

        return json.dumps(value, use_decimal=True)

    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return self.get_prep_value(value)
