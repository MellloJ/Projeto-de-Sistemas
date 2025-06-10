from rest_framework import serializers
from django.core.exceptions import ValidationError
import re

def calcDigito(digs):
    s = sum(int(digs[i]) * ((len(digs) + 1) - i) for i in range(len(digs)))
    res = 11 - s % 11
    return '0' if res >= 10 else str(res)

def validate_cpf(self, value):

    cpf = re.sub(r'\D', '', value)

    if len(cpf) != 11 or cpf == cpf[0] * 11:
        raise serializers.ValidationError("CPF inválido.")

    d1 = calcDigito(cpf[:9])
    d2 = calcDigito(cpf[:9] + d1)

    if cpf[-2:] != d1 + d2:
        raise serializers.ValidationError("CPF inválido.")

    return cpf