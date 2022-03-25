from allauth.account.adapter import DefaultAccountAdapter


class CustomAccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=False):
        user = super().save_user(request, user, form, commit)
        data = form.cleaned_data
        user.address = data.get('address')
        user.firstname=data.get('firstname')
        user.lastname=data.get('lastname')
        user.phonenumber=data.get('phonenumber')
        user.dob=data.get('dob')
        
        user.save()
        return user