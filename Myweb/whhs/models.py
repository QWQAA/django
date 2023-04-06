from django.db import models


# Create your models here.

class StudentInfo(models.Model):

    stu_id = models.UUIDField(primary_key=True, max_length=10)
    stu_user = models.CharField(max_length=20, null=False)
    stu_pwd = models.CharField(max_length=20, null=False)
