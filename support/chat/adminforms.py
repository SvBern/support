from django import forms


class MessageStatusForm(forms.ModelForm):
    def clean(self):
        if self.cleaned_data.get('is_answer') == False:
            raise forms.ValidationError('Field "is_answer" must be "True"')
