from django.shortcuts import render, redirect
from blog.models import Post, Coment
from blog.forms import upload_form

# Create your views here.
def main_page(request):
    posts = Post.objects.all()
    return render(request, "blog/main.html", {"posts": posts})


def current(request, pk):
    post = Post.objects.get(pk=pk)
    coments = Coment.objects.all()

    if request.POST:
        form = upload_form(request.POST, request.FILES)

        if form.is_valid():
            form.save()
    print(request.POST)
    return render(
        request,
        "blog/current.html",
        {"post": post, "coments": coments, "form": upload_form},
    )
