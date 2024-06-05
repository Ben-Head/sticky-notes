from django import forms
from django.contrib.auth.models import User
from .models import Post

class UserRegistrationForm(forms.ModelForm):
    # Custom user registration form with password field
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        # Define the form's meta properties
        model = User  # Form is based on the User model
        fields = ['username', 'email', 'password']  # Fields to include in the form

    def __init__(self, *args, **kwargs):
        # Customize form initialization
        super().__init__(*args, **kwargs)
        # Add Bootstrap form-control class to all form fields
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

class PostForm(forms.ModelForm):
    # Form for creating and updating posts
    class Meta:
        # Define the form's meta properties
        model = Post  # Form is based on the Post model
        fields = ['title', 'content']  # Fields to include in the form

    def __init__(self, *args, **kwargs):
        # Customize form initialization
        super().__init__(*args, **kwargs)
        # Add Bootstrap form-control class to all form fields
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
