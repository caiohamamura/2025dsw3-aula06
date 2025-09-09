from django.shortcuts import redirect, render
from . import models
from instacaio.forms import PostForm

# Create your views here.
def inicio(req):
    return render(req, 'inicio.html')

def controle(req):
    return render(req, 'controle.html', {
        'variavel': range(10)
    })

def postar(req):
    if req.method == "POST":
        form = PostForm(req.POST, req.FILES)
        if form.is_valid():
            form.save()
            return redirect("inicio")
    else:
        form = PostForm()

    return render(req, "postar.html", {"formulario": form})

def ver_postagens(req):
    todos_posts = models.Post.objects.filter(aprovado=True).all()
    return render(req, 'listar_posts.html', {
        'postagens': todos_posts
    })