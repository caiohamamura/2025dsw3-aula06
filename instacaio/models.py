from django.db import models

class Post(models.Model):
    autor = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to="posts/", blank=True, null=True)
    mensagem = models.TextField()