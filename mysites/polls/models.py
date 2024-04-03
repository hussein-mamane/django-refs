from datetime import timedelta  # , timezone
from django.db import models
from django.utils import timezone
# Create your models here.


class Question(models.Model):
    # machine-readable name for python and the database
    question_text = models.CharField(max_length=200)
    # human-readable name, doubles documentation
    pub_date = models.DateTimeField("date published")

    # adding methods only need a new shell to be visible
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - timedelta(days=1)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
