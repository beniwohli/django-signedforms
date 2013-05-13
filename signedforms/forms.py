# -*- coding: utf-8 -*-
from django import forms
from django.db import models
from django.core import signing
from django.utils.translation import ugettext_lazy as _


class SignedFormBase(object):
    bad_signature_error = _("Please leave the hidden fields alone. Thanks!")
    signed_fields = None

    def __init__(self, *args, **kwargs):
        if not 'initial' in kwargs and 'data' in kwargs and 'signature' in kwargs['data']:
            try:
                kwargs['initial'] = signing.loads(kwargs['data']['signature'])
            except signing.BadSignature:
                # TODO: is there anything useful we can do here?
                pass

        super(SignedFormBase, self).__init__(*args, **kwargs)
        self.fields['signature'] = forms.CharField(widget=forms.HiddenInput, required=True)
        if self.signed_fields:
            data = {field: self.initial.get(field) for field in self.signed_fields}
            for k, v in data.iteritems():
                if isinstance(v, models.Model):
                    data[k] = v.pk
            self.fields['signature'].initial = signing.dumps(data)
            self.initial['signature'] = self.fields['signature'].initial
            for field in self.signed_fields:
                self.fields[field].widget = forms.HiddenInput()
        else:
            self.fields['signature'].required = False

    def clean_signature(self):
        try:
            return signing.loads(self.cleaned_data['signature'])
        except signing.BadSignature:
            raise forms.ValidationError(self.bad_signature_error)

    def clean(self):
        if self.signed_fields:
            data = dict((field, self.data.get(field)) for field in self.signed_fields)
            signed_data = self.cleaned_data['signature']
            for key, value in data.items():
                signed_value = unicode(signed_data[key]) if signed_data[key] is not None else ''
                if signed_value != value:
                    print signed_value, value
                    raise forms.ValidationError(self.bad_signature_error)
        return self.cleaned_data


class SignedForm(SignedFormBase, forms.Form):
    pass


class SignedModelForm(SignedFormBase, forms.ModelForm):
    pass
