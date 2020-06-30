from django import forms
from .models import Dated_Entry, Titled_Entry, Text_Entry

class Dated_Form(forms.ModelForm):

    class Meta:
        model = Dated_Entry
        fields = ('title', 'start_date', 'end_date', 'ended', 'text', 'type_id',)


class Titled_Form(forms.ModelForm):

    class Meta:
        model = Titled_Entry
        fields = ('title', 'text', 'type_id',)


class Text_Form(forms.ModelForm):

    class Meta:
        model = Text_Entry
        fields = ('text', 'type_id',)
