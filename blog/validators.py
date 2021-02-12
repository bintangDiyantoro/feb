from django.core.exceptions import ValidationError
import re


def validateWriter(value):
    if re.findall('ot.*ng', value, re.IGNORECASE):
        raise ValidationError("Plis Otong jangan ikut2an nulis, dia belum cukup umur")