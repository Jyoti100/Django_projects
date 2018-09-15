from django import forms
from django.core.exceptions import ValidationError
from .models import Author, Tag, Category, Post, Feedback
from django.template.defaultfilters import slugify
from datetime import datetime
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm

class AuthorForm(forms.ModelForm):
    class Meta:
        model=Author
        fields ='__all__'

    def clean_name(self):
        name = self.cleaned_data['name']
        name_l = name.lower()
        if name_l == "admin" or name_l == "author":
            raise ValidationError("Author name can't be 'admin/author'")
        return name_l

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        print("emial", email)
        r =Author.objects.filter(email=email).count()
        print("COunt is ", r)
        if r > 0:
            raise ValidationError("{0} is already exists".format(email))
        return email.lower()


    def save(self):
        new_author = Author.objects.create(
            name= self.cleaned_data['name'],
            email = self.cleaned_data['email'],
            active = self.cleaned_data['active'],
            creation_date = self.cleaned_data['creation_date'],
            last_logged_in = self.cleaned_data['last_logged_in']
        )
        print("New author ", new_author)
        return new_author

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'

    def clean_name(self):
        n = self.cleaned_data['name']
        if n.lower() == "tag" or n.lower() == "add" or n.lower() == "update":
            raise ValidationError("Tag name can't be '{}'".format(n))
        return n

    def clean_slug(self):
        return self.cleaned_data['slug'].lower()

class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = '__all__'

    def clean_name(self):
        n = self.cleaned_data['name']
        if n.lower() == "tag" or n.lower() == "add" or n.lower() == "update":
            raise ValidationError("Category name can't be '{}'".format(n))
        return n

    def clean_slug(self):
        return self.cleaned_data['slug'].lower()

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'content', 'author', 'category', 'tags',)

    def clean_name(self):
        n = self.cleaned_data['title']
        if n.lower() == "post" or n.lower() == "add" or n.lower() == "update":
            raise ValidationError("Post name can't be '{}'".format(n))
        return n

    def clean(self):
        cleaned_data = super(PostForm, self).clean()  # call the parent clean method
        title = cleaned_data.get('title')
        # if title exists create slug from title
        if title:
            cleaned_data['slug'] = slugify(title)
        return cleaned_data

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'

