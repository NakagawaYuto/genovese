from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import(LoginView, LogoutView)
from login.forms import CommentForm, LoginForm
from .models import Post
# Create your views here.
def frontpage(request):
  posts = Post.objects.all()
  return render(request, "login/frontpage.html", {"posts": posts})


def post_detail(request, slug):
  post = Post.objects.get(slug=slug)

  if request.method == "POST":
    form = CommentForm(request.POST)

    if form.is_valid():
      comment = form.save(commit=False)
      comment.post = post
      comment.save()

      return redirect("login:post_detail", slug=post.slug)
  else:
    form = CommentForm()
  return render(request, "login/post_detail.html", {"post": post, "form": form})


class Login(LoginView):
  #ログインページ
  form_class = LoginForm
  template_name = 'login.html'


class Logout(LoginRequiredMixin, LogoutView):
  #ログアウトページ
  template_name = 'login.html'