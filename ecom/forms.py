from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class CLog(forms.Form):
    username=forms.CharField(max_length=100)
    password=forms.CharField(widget=forms.PasswordInput)
    def clean(self):
        u=self.cleaned_data.get("username")    
        p=self.cleaned_data.get("password")        
        try:
            User.objects.get(username=u)
        except:
            raise forms.ValidationError("Username does not exist")
        try:
           User.objects.get(username=u,password=p) 

        except:
            raise forms.ValidationError(" password is not correct")


class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username",'first_name', "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user