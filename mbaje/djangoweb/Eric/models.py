from django.db import models


# Create your models here.
class Sender(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    imageUrl = models.CharField(max_length=250)
    def __str__(self):
        return self.name

class Message(models.Model):
    sender = models.CharField(max_length=200)
    recipient = models.CharField(max_length=200)
    message = models.CharField(max_length=200)
    visible = models.IntegerField(default=1)
    timestamp = models.DateTimeField('date created')
    def __str__(self):
        return self.message


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)



class Question(models.Model):
    # ...
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    # ...
    def __str__(self):
        return self.choice_text

        import datetime


from django.utils import timezone


class Question(models.Model):
    # ...
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)