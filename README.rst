==================
django-signedforms
==================

A small library that provides a form class that signs a configurable set of
hidden fields using ``django.core.signing``.

The most common use case for such a form is when the view that handles the post
differs from the view that sets up the form, but you need to pass some
information from one view to the other, without evil hackers tampering with your
precious data.

Usage
=====

Subclass SignedForm, and define which fields should be signed::

    from signedforms.forms import SignedForm

    class MyForm(SignedForm):
        signed_fields = ['redirect_url',]

        redirect_url = forms.CharField(required=False, widget=forms.HiddenInput)

In the form that sets up the view, provide the data to be signed in the
``initial`` dictionary::

    my_form = MyForm(initial={'redirect_url': self.request.path_info})

and in the view that handles the posted form::

    def form_valid(self, form):
        # do some work
        return HttpResponseRedirect(form.cleaned_data['redirect_url'])

.. note::

    If the user tampered with the hidden data, the form will not validate.

.. warning::

    Only fields that contain JSON-serializable data can be signed. This includes
    all fields that are represented as text in the database, but not datetimes
    and other more "complex" types.
