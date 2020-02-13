import pytest
import sys
sys.path.append('../translate')

from translate_number import TranslateNumber, TranslateNumberException


def test_invalid_number_string():
    with pytest.raises(TranslateNumberException, match="Valor invalido! Sao permitidos apenas numeros inteiros entre -99999 a 99999."):
        TranslateNumber('123aaaa')


def test_invalid_number_other_range():
    with pytest.raises(TranslateNumberException, match="Fora da faixa permitida! Tente algum numero entre -99999 a 99999."):
        TranslateNumber('100000')


def test_invalid_number_other_range_negative():
    with pytest.raises(TranslateNumberException, match="Fora da faixa permitida! Tente algum numero entre -99999 a 99999."):
        TranslateNumber('-200000')


def test_invalid_number_real():
    with pytest.raises(TranslateNumberException, match="Valor invalido! Sao permitidos apenas numeros inteiros entre -99999 a 99999."):
        TranslateNumber('1.5')

def test_invalid_number_real_negative():
    with pytest.raises(TranslateNumberException, match="Valor invalido! Sao permitidos apenas numeros inteiros entre -99999 a 99999."):
        TranslateNumber('-1345.89')

def test_valid_number():
    TranslateNumber('100')


def test_number_1():
    t = TranslateNumber('1')
    assert t.translate() == 'um'

def test_number_19():
    t = TranslateNumber('19')
    assert t.translate() == 'dezenove'

def test_number_254():
    t = TranslateNumber('254')
    assert t.translate() == 'duzentos e cinquenta e quatro'

def test_number_0():
    t = TranslateNumber('0')
    assert t.translate() == 'zero'

def test_number_6699():
    t = TranslateNumber('-6699')
    assert t.translate() == 'menos seis mil seiscentos e noventa e nove'

def test_number_100():
    t = TranslateNumber('100')
    assert t.translate() == 'cem'

def test_number_67329():
    t = TranslateNumber('67329')
    assert t.translate() == 'sessenta e sete mil trezentos e vinte e nove'

def test_number_10110():
    t = TranslateNumber('10110')
    assert t.translate() == 'dez mil cento e dez'

def test_number_15012():
    t = TranslateNumber('15012')
    assert t.translate() == 'quinze mil e doze'

def test_number_1000_whiteSpace():
    t = TranslateNumber(' 1000 ')
    assert t.translate() == 'mil'
