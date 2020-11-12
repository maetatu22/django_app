from django import forms

class HelloForm(forms.Form):
    data = [
          ('one', 'radio 1'),
          ('two', 'radio 2'),
          ('three', 'radio 3'),
          ('four', 'item 5'),
          ('five', 'item 5'),
    ]
    choice = forms.ChoiceField(label='radio', \
            choices=data, widget=forms.Select(attrs={'size': 5}))