# -*- coding: utf-8 -*-
import datetime
from copy import copy

from django import forms
from django.utils import unittest

from signedforms.forms import SignedForm


class MyForm(SignedForm):
    signed_fields = ['redirect_url',]
    redirect_url = forms.CharField(required=False, widget=forms.HiddenInput)


class SignedFormTestCase(unittest.TestCase):
    def setUp(self):
        self.redirect_url = 'test'
        self.timestamp = datetime.datetime.now()
        self.form = MyForm(initial={'redirect_url': self.redirect_url})

    def test_untampered(self):
        form = MyForm(data=self.form.initial)
        assert form.is_valid()

    def test_tampered(self):
        tampered = copy(self.form.initial)
        tampered['redirect_url'] = 'test'
        form = MyForm(data=tampered)
        assert not form.is_valid()
