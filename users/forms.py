from .models import CustomUser
from django.forms import ModelForm,Form

class CustomUserCreateForm(ModelForm):
    class Meta:
        model=CustomUser
        fields=['username','first_name','last_name','email','password','image']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
    # def save(self, commit=True):
    #     user=super().save(commit)
    #     user.set_password(self.cleaned_data['password'])
    #     user.save()
    #     return user

class CustomUserUpdateForm(ModelForm):
    class Meta:
        model=CustomUser
        fields=['username','first_name','last_name','email','image']



# class CustomUserBaseForm(ModelForm):
#     class Meta:
#         model = CustomUser
#         fields = ['username', 'first_name', 'last_name', 'email', 'image']
#
# class CustomUserCreateForm(CustomUserBaseForm):
#     class Meta(CustomUserBaseForm.Meta):
#         fields = CustomUserBaseForm.Meta.fields + ['password']
#
#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.set_password(self.cleaned_data['password'])
#         if commit:
#             user.save()
#         return user
#
# class CustomUserUpdateForm(CustomUserBaseForm):
#     pass  # No need to define Meta again, inherits from CustomUserBaseForm.Meta