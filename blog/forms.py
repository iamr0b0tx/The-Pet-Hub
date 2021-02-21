from .models import Comment, Post
from django import forms

from .widgets import CustomClearableFileInput


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     categories = User.objects.all()
    #     friendly_names = [(c.id, c.get_friendly_name()) for c in categories]
    #
    #     self.fields['category'].choices = friendly_names
    #     for field_name, field in self.fields.items():
    #         field.widget.attrs['class'] = 'border-black rounded-0'
