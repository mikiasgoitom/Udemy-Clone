# single_file_django.py

import os
import sys
from django.conf import settings
from django.core.management import execute_from_command_line
from django.db import models
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import path, re_path
from django.template import engines
from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from django.utils.html import escape
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect

#URL patterns 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', item_list, name='item_list'),
    path('item/<int:pk>/', item_detail, name='item_detail'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('item/<int:item_id>/comment/', add_comment, name='add_comment'),
]

# Configuration settings
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

settings.configure(
    DEBUG=True,
    SECRET_KEY='your-secret-key',
    ROOT_URLCONF=__name__,
    ALLOWED_HOSTS=[],
    INSTALLED_APPS=[
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
    ],
    MIDDLEWARE=[
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'path.to.SimpleMiddleware',
    ],
    TEMPLATES=[
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.path.join(BASE_DIR, 'templates')],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ],
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    },
    STATIC_URL='/static/',
)

# middleware for the comments 
class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

# Models
class Item(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Admin
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at')

# Views
def item_list(request):
    items = Item.objects.all()
    return render(request, 'item_list.html', {'items': items})

def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'item_detail.html', {'item': item})

# URL Configuration
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', item_list, name='item_list'),
    path('item/<int:pk>/', item_detail, name='item_detail'),
]

# Templates setup
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
os.makedirs(TEMPLATES_DIR, exist_ok=True)

# views.py
from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form})

def post_update(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_form.html', {'form': form})

def post_delete(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect('post_list')

with open(os.path.join(TEMPLATES_DIR, 'item_list.html'), 'w') as f:
    f.write(item_list_html)

with open(os.path.join(TEMPLATES_DIR, 'item_detail.html'), 'w') as f:
    f.write(item_detail_html)



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content')

# Admin site setup
admin.autodiscover()
admin.site.register(Item, ItemAdmin)

if __name__ == "__main__":
    if 'runserver' in sys.argv:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', __name__)
        execute_from_command_line(sys.argv)
    elif 'migrate' in sys.argv or 'makemigrations' in sys.argv:
        execute_from_command_line(sys.argv)
    else:
        print("Usage: python single_file_django.py runserver|migrate|makemigrations")

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput, label='Confirm password')

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                return redirect('item_list')
            else:
                return HttpResponse('Invalid login')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')

# Comment model
class Comment(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.item.name}'

#Comment Form 
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)

#comment view
def add_comment(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.item = item
            comment.user = request.user
            comment.save()
            return redirect('item_detail', pk=item_id)
    else:
        form = CommentForm()
    return render(request, 'add_comment.html', {'form': form})