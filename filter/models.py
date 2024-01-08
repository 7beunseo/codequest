from django.db import models

# Create your models here.
class Stack(models.Model):
    class Meta:
        db_table='stack'
    title=models.CharField(max_length=100, default='')

class CodeQuest(models.Model):
    class Meta:
        db_table='codequest'
    number=models.CharField(max_length=100, default='')
    title=models.CharField(max_length=100, default='')
    explanation=models.TextField()
    purpose=models.CharField(max_length=100)
    stacks=models.ManyToManyField(Stack, related_name='codequests')
    year=models.CharField(max_length=100, default='')