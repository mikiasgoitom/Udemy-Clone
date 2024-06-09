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

item_list_html = """
<!DOCTYPE html>
<html>
<head>
    <title>Item List</title>
</head>
<body>
    <h1>Item List</h1>
    <ul>
        {% for item in items %}
            <li><a href="{% url 'item_detail' item.pk %}">{{ item.name }}</a></li>
        {% endfor %}
    </ul>
</body>
</html>
"""

item_detail_html = """
<!DOCTYPE html>
<html>
<head>
    <title>{{ item.name }}</title>
</head>
<body>
    <h1>{{ item.name }}</h1>
    <p>{{ item.description }}</p>
    <p>Created at: {{ item.created_at }}</p>
    <a href="{% url 'item_list' %}">Back to list</a>
</body>
</html>
"""

with open(os.path.join(TEMPLATES_DIR, 'item_list.html'), 'w') as f:
    f.write(item_list_html)

with open(os.path.join(TEMPLATES_DIR, 'item_detail.html'), 'w') as f:
    f.write(item_detail_html)

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