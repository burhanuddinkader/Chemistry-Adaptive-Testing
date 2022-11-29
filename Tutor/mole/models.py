from django.db import models
import uuid

# Create your models here.
# class BaseModel(models.Model):
#     uid=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     created_at=models.DateField(auto_now_add=True)
#     updated_at=models.DateField(auto_now_add=True)

    # class Meta:
    #     abstract = True

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

    # def get_ans(self):
    #     answere_objs=list(Answere.objects.filter(question_answere=self))
    #     data=[]
    #     # random.shuffle(answere_objs)
    #     for answere_obj in answere_objs:
    #         data.append({
    #             "answere":answere_obj.answere,
    #             "is_correct":  answere_obj.is_correct
    #         })
    #     return data

class Answere(models.Model):
    question_ans=models.ForeignKey(Question,on_delete=models.CASCADE)
    answere=models.CharField(max_length=200)
    isCorrect=models.BooleanField(default=False)

    def __str__(self):
        return self.answere
