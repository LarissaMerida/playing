from django.db import models

# Create your models here.

class Music(models.Model):
    class Meta:

        db_table = 'music'
    
    title = models.CharField(max_length=200)
    seconds = models.IntegerField()

    def __str__(self):
        return self.title
    

class Album(models.Model):

    class Meta:
        db_table = 'album'

    title = models.CharField(max_length=200)
    band = models.ForeignKey('Band', related_name='albuns', on_delete=models.CASCADE)
    date = models.DateField()


class Band(models.Model):

    class Meta:
        db_table = 'band'

    name = models.CharField(max_length=200)

class Member(models.Model):

    class Meta:
        db_table = 'member'

    name = models.CharField(max_length=200)
    age = models.IntegerField()
    bancd = models.ForeignKey('Band', related_name ='members', on_delete=models.CASCADE)
