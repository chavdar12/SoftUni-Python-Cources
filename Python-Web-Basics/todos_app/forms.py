from django import forms


class TodoForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (field_name, field) in self.fields.items():
            if 'class' in field.widget.attrs:
                value = field.widget.attrs['class'] + ' form-control'
            else:
                value = ' form-control'
            field.widget.attrs['class'] = value

    def clean_bot_catcher(self):
        if self.cleaned_data['bot_catcher']:
            raise forms.ValidationError('This is a bot')

    title = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'class': '',
            }),
        required=True)

    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': '',
            }),
        required=False)

    bot_catcher = forms.CharField(
        widget=forms.HiddenInput,
        required=False
    )
