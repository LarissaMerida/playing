from django.shortcuts import render

# Create your views here.
class Profile(models.Model):
    first_name = models.CharField()
    last_name = models.CharField()
    interest = models.CharField()

class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    interest = forms.CharField(required=True)

class Meta:
    model = Profile