from django.shortcuts import redirect, render
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