from django.contrib.auth.models import AbstractUser
from django.db import models
from rest_framework import serializers


class User(AbstractUser):
    pass

class Post(models.Model):
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)



class ReactionsCategory(models.Model):
    emoji = models.CharField(max_length=10)

class ReactionPost(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    emoji = models.ForeignKey(ReactionsCategory, on_delete=models.CASCADE)

class Follower(models.Model):
    seguidor = models.ForeignKey(User, related_name='seguidos', on_delete=models.CASCADE)
    seguido = models.ForeignKey(User, related_name='seguidores', on_delete=models.CASCADE)



class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
