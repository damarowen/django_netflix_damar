from django.forms import ModelForm

from netflix.models import Profile

class ProfileForm(ModelForm):
    class Meta:
        model=Profile
        #not catch uuid from post
        exclude=['uuid']