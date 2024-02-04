from django.db import models

# Create your models here.
class Profile(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200, default='Tester')
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    summary = models.TextField(max_length=2000)

    university1 = models.CharField(max_length=200)
    university_qualification1 = models.CharField(max_length=200)
    university_address1 = models.CharField(max_length=200)
    university_date1 = models.CharField(max_length=200)

    university2 = models.CharField(max_length=200)
    university_qualification2 = models.CharField(max_length=200)
    university_address2 = models.CharField(max_length=200)
    university_date2 = models.CharField(max_length=200)

    previous_work1 = models.TextField(max_length=1000)
    previous_work1_pos = models.TextField(max_length=1000)
    previous_work1_loc = models.TextField(max_length=1000)
    previous_work1_date = models.TextField(max_length=1000)
    previous_work1_role = models.TextField(max_length=1000)

    previous_work2 = models.TextField(max_length=1000)
    previous_work2_pos = models.TextField(max_length=1000)
    previous_work2_loc = models.TextField(max_length=1000)
    previous_work2_date = models.TextField(max_length=1000)
    previous_work2_role = models.TextField(max_length=1000)

    skill1 = models.TextField(max_length=1000)
    skill2 = models.TextField(max_length=1000)
    skill3 = models.TextField(max_length=1000)
    skill4 = models.TextField(max_length=1000)

    project1 = models.TextField(max_length=1000)
    project1_desc = models.TextField(max_length=1000)
    project2 = models.TextField(max_length=1000)
    project2_desc = models.TextField(max_length=1000)

    interests = models.TextField(max_length=1000)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
