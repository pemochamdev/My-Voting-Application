from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import authenticate, login, logout

from voteapp.models import Category, CategoryItem

# Create your views here.

def index(request):
    categories = Category.objects.all().order_by('-created_at')
    template_name = 'index.html'
    context = {
        'categories': categories,
    }
    return render(request, template_name, context)

def detail(request, slug):
    category = Category.objects.get(slug=slug)
    category_items = CategoryItem.objects.filter(category=category)
    template_name = 'detail.html'
    
    
    msg = False

    if request.user.is_authenticated:
        
        if category.voters.filter(id=request.user.id).exists():
            msg = True
            
    
    print(msg)

    
    if request.method == 'POST':
        selected_id = request.POST['category_item']
        print(selected_id)
        item = CategoryItem.objects.get(id=selected_id)
        print(item)
        item.total_vote += 1
        category_item = item.category
        category_item.total_vote +=1
        item.voters.add(request.user)
        item.category.voters.add(request.user)
        item.save()
        category_item.save()
        
    context = {
        'category': category,
        'category_items': category_items,
        'msg': msg,
    }
    return render(request, template_name, context)

def result(request):
    template_name = 'result.html'
    context = {}
    return render(request, template_name, context)


def signup(request):

    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('signin')
    
    template_name = 'signup.html'
    context = {
        'form':form
    }
    return render(request, template_name, context)


def signin(request):
    template_name = 'signin.html'
    context = {}
    return render(request, template_name, context)

class CoustomLoginView(LoginView):
    template_name = 'signin.html'
    success_url ='index'
    def get_success_url(self) -> str:
        return reverse(self.success_url)


class CoustomLogoutView(LogoutView):
    #template_name = 'logout.html'
    success_url ='index'
    def get_success_url(self) -> str:
        return reverse(self.success_url)


def log_out(request):
    logout(request)
    return redirect('index')