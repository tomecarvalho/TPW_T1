from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Group


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class PaymentForm(forms.Form):
    CHOICES = (('MasterCard', 'MasterCard'), ('Visa', 'Visa'), ('Paypal', 'Paypal'))
    card = forms.ChoiceField(choices=CHOICES)
    number = forms.IntegerField(max_value=9999999999999999, min_value=1000000000000000,
                                widget=forms.TextInput(attrs={'placeholder': 'Card Number'}))
    date = forms.DateField(widget=forms.TextInput(attrs={'placeholder': '00/00/00'}))
    name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    cvc = forms.IntegerField(min_value=100, max_value=999, widget=forms.TextInput(attrs={'placeholder': 'CVC'}))


class SearchForm(forms.Form):
    CATEGORIES = (('', '----------'), ('Pants', 'Pants'), ('Jeans', 'Jeans'), ('Shirts', 'Shirts'), ('Jackets', 'Jackets'), ('Underwear', 'Underwear'))
    by_category = forms.ChoiceField(choices=CATEGORIES, required=False)
    all_groups = Group.objects.all()
    group_list = [('', '----------')]
    for group in all_groups:
        group_list.append((group.name, group.name))
    GROUPS = tuple(group_list)
    by_group = forms.ChoiceField(choices=GROUPS, required=False)
    by_price_Lower = forms.IntegerField(required=False, label="Lower Limit")
    by_price_Lower.widget.attrs.update({'style': 'width: 3em'})
    by_price_Upper = forms.IntegerField(required=False, label="Upper Limit")
    by_price_Upper.widget.attrs.update({'style': 'width: 3em'})

