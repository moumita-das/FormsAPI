from django.forms import ModelForm,TextInput,DateInput,CharField,PasswordInput
from django.contrib.auth.models import User
from .models import ItemList

class ItemForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ItemForm, self).__init__(*args, **kwargs)

    class Meta:
        model =ItemList
        fields = ['fname','lname','dob','img']
        widgets = {
            'fname': TextInput(attrs={'placeholder': 'First Name'}),
            'lname': TextInput(attrs={'placeholder': 'Last Name'}),
            'dob': DateInput(attrs={'placeholder': 'mm/dd/yyyy'}),
        }

    def clean(self):
        super(ItemForm,self).clean()
        fname = self.cleaned_data.get('fname')
        lname = self.cleaned_data.get('lname')
        img = self.cleaned_data.get('img',False)

        if not fname.isalpha():
            self._errors['fname'] = self.error_class([
                'Only letters allowed in first name'])
        if not lname.isalpha():
            self._errors['lname'] = self.error_class([
                'Only letters allowed in last name'])
        return self.cleaned_data


class UserForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
    password = CharField(widget=PasswordInput())
    class Meta():
        model = User
        fields = ['username','password']
    def clean(self):
        super(UserForm,self).clean()
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        return self.cleaned_data