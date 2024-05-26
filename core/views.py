from django.shortcuts import render

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

def home(request):
    return render(request, "home.html")
def register(request):
    return render(request, "registration/register.html", {"form": form})
