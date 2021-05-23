from django import forms
from bulma_widget import widgets
from .models import Trip, Gear, Message


class TripForm(forms.ModelForm):

    # participants = forms.ModelMultipleChoiceField(queryset=User.objects.all(), required=False, widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Trip
        exclude = ['creator']
        template_name = 'dashboard.html'
        widgets = {
            'name': widgets.BulmaTextInput(attrs={'class': 'field', 'type': 'text'}),
            'participants': widgets.BulmaMultiSelect(attrs={'class': 'field-control'}),
            'start_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'field mt-4', 'type': 'date'}),
            'end_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'field mt-4', 'type': 'date'}),
        }


class GearForm(forms.ModelForm):
    class Meta:
        model = Gear
        exclude = ['owner', 'trips']
        template_name = 'gear.html'
        widgets = {
            'name': widgets.BulmaTextInput(attrs={'class': 'field is-half', 'type': 'text'}),
            'category': widgets.BulmaSelect(attrs={'class': 'field', 'type': 'text'}),
            'link': widgets.BulmaTextInput(attrs={'class': 'field is-fullwidth', 'type': 'text'}),
            # 'photo': widgets.BulmaFileInput(attrs={'class': 'file', 'type': 'file'}),
        }
        


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'
        template_name = 'dashboard.html'