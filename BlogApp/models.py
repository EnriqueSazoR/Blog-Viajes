from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Modelo Categoria
class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        

# Modelo Publicacion
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    published_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    travel_destination = models.CharField(max_length=30)
    image = models.ImageField(upload_to='posts/', null=True, blank=True)
    slug = models.SlugField(max_length=100, unique=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Publicación"
        verbose_name_plural = "Publicaciones"
        

# Modelo Comentarios
class Comment(models.Model):
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    published_date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    
    def __str__(self):
        return f"Comentario de {self.author} en {self.post}"
    
    class Meta:
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"
