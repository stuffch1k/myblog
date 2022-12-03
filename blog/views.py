from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.views.generic.edit import FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.urls import reverse, reverse_lazy

from .models import *
from .forms import *


# Create your views here.
def index(request):
    posts=Blog.objects.all()
    categories=Category.objects.all()
    active=-1
    return render(request, 'blog/index.html',{'title':'Главная страница','posts':posts, 'categories':categories,'active':active})

class HomeView(ListView):
    model=Blog
    template_name='blog/index.html'
    context_object_name='posts'

    def get_context_data(self, *, object_list=None,**kwargs):
        context=super().get_context_data(**kwargs)
        context['categories']= Category.objects.all()
        context['title']='Главная страница'
        context['active']=-1
        return context

class CategoryView(ListView):
    model=Blog
    template_name='blog/index.html'
    context_object_name='posts'
    def get_context_data(self, *, object_list=None,**kwargs):
        context=super().get_context_data(**kwargs)
        context['categories']= Category.objects.all()
        context['title']=f"Cтраница категории {Category.objects.get(slug=self.kwargs['slug']).name}"
        context['active']=self.kwargs['slug']
        return context
    def get_queryset(self,*args,**kwargs):
        return Blog.objects.filter(category__slug=self.kwargs['slug'])


#         return context

# def post_categories(request,cat):
#     posts = Blog.objects.filter(category__slug=cat)
#     categories=Category.objects.all()
#     active=Category.objects.get(slug=cat).slug
#     return render(request, 'blog/index.html', {'title':'Main page', 'posts':posts, 'category':categories,'active':active} )

def about(request):
    return render(request, 'blog/about.html',{'title':'O нас'})

class DetailView(DetailView):
    model=Blog
    template_name='blog/post.html'
    context_object_name='post'
    # def get_context_data(self, *, object_list=None,**kwargs):
        # context=super().get_context_data(**kwargs)
#         context['title']=context['post'].title
#         return context

# def post_detail(request,pk):
#     post=Blog.objects.get(pk=pk)
#     return render(request,'blog/post.html',{'title':post.title,'post':post})

class ProfileView(DetailView):
    model=CustomUser
    template_name='blog/my_profile.html'
    pk_url_kwarg = 'pk'
    context_object_name='user'
   


# def category_view(request, slug):
#     categories=Category.objects.all()
#     posts=Blog.objects.filter(category__slug=slug)
#     active=slug
#     return render(request, 'blog/index.html',{'title':f'Страница категории {Category.objects.get(slug=slug).name}', 'posts':posts, 'categories':categories,'active':active})

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
def add_post(request):
    if request.method == 'POST':
        form=AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                return redirect('home')
            except:
                form.add_error(None,'Ошибка')
    else:
        form=AddPostForm()
    return render(request,'blog/add_post.html', {'form':form, 'title':'Добавление записи'})

class AddPost(CreateView):
    model=Blog
    form_class=AddPostForm
    template_name='blog/add_post.html'
    context_object_name='form'  

    success_url=reverse_lazy('home')  

class AddCategory(CreateView):
    model=Category
    form_class=AddCategoryForm
    template_name='blog/add_category.html'
    context_object_name='form'

    success_url=reverse_lazy('home')

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name= 'blog/register.html'
    success_url =  reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)
        context['title']='Регистрация пользователя'
        return context

    def form_valid(self,form):
        user=form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(LoginView):
    form_class= LoginUserForm
    template_name='blog/login.html'

    def get_success_url(self):
        return reverse_lazy('home')

def logout_user(request):
    logout(request)
    return redirect("home")



