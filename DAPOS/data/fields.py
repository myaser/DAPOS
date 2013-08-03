from django.db import models
import re


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
