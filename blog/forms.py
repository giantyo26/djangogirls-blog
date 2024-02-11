from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            "title",
            "text",
        )

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        text = cleaned_data.get("text")

        if len(title) <= 3:
            raise forms.ValidationError("Title must have more than 3 characters")

        if title and text:
            if title.isupper() != text.isupper():
                raise forms.ValidationError("Title and Text must be in the same case")

        return cleaned_data
