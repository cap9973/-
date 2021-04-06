from django import forms
from . import models

class PostCreateForm(forms.ModelForm):
    class Meta:
        model=models.PostModel
        fields='__all__'

    # def save(self, pk, *args, **kwargs):
    #     photo = super().save(commit=False)
    #     img=self.models.PostModel.get(pk=pk)
    #     photo.user_id=img
    #     photo.save()


class PostUpdateForm(forms.ModelForm):
    class Meta:
        model=models.PostModel
        fields=('content', 'images')














