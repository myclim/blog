from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login


from main.models import *
from main.forms import (
    PostCreateForm,
    PostUpdateForm,
    UserAuthenticationForm,
    UserRegisterForm,
)
from django.contrib.auth import get_user_model
from main.utils import search



class PostsView(ListView):
    model = Posts
    template_name = "main/index.html"
    paginate_by = 6
    context_object_name = "blogs"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_user_id"] = self.request.user.id
        return context
    
    def get_queryset(self):
        query = super().get_queryset()
        q_item = self.request.GET.get('q', None)

        if q_item:
            query = search(q_item)
        return query
            


class PostsDetail(DetailView):
    model = Posts
    template_name = "main/detail.html"
    context_object_name = "post"
    slug_field = "id"
    slug_url_kwarg = "pk"

    def get_object(self, queryset=None):
        post = super().get_object(queryset)
        post.views += 1
        post.save()
        return post


class CreatePosts(CreateView):
    model = Posts
    template_name = "main/create.html"
    form_class = PostCreateForm
    success_url = reverse_lazy("main")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class UpdatePosts(LoginRequiredMixin, UpdateView):
    model = Posts
    form_class = PostUpdateForm
    template_name = "main/update.html"
    slug_field = "id"
    slug_url_kwarg = "pk"

    def form_valid(self, form):
        post = self.get_object()
        user = self.request.user
        if user == post.user:
            form.save()
            return super().form_valid(form)
        return super().form_invalid(form)

    def get_success_url(self):
        post = self.get_object()
        return reverse_lazy("detail", kwargs={"pk": post.pk})


@login_required
def delete_post(request, pk):
    if request.method == "POST":
        user = request.user
        item = get_object_or_404(Posts, user=user, pk=pk)
        item.delete()
    return redirect('/')


class UserCreateView(CreateView):
    model = get_user_model()
    template_name = "main/user/register.html"
    form_class = UserRegisterForm
    success_url = reverse_lazy("main")

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        login(self.request, user)
        return response


@login_required
def log_out(request):
    logout(request)
    return redirect('/')


def user_login(request):
    if request.method == "POST":
        form = UserAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = UserAuthenticationForm()

    return render(request, 'main/user/auth.html', {'form': form})
