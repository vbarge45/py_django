from django.db import models

# Create your models here.

class RequestDetails(models.Model):
    user_id = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    project_name = models.CharField(max_length=100)
    project_name = models.CharField(max_length=100)
    project_type = models.CharField(max_length=100)
    manager_name = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)