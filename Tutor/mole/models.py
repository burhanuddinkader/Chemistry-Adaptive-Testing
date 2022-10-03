from django.db import models

# Create your models here.


class Category(models.Model):
    category_name=models.CharField(max_length=200)

    def __str__(self):
        return self.category_name
class Question(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)   
    question=models.CharField(max_length=200)
    marks=models.IntegerField(default=5)

    def __str__(self):
        return self.question

class Answere(models.Model):
    question_ans=models.ForeignKey(Question,on_delete=models.CASCADE)
    answere=models.CharField(max_length=200)
    isCorrect=models.BooleanField(default=False)

    def __str__(self):
        return self.answere
