from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))
GENDER = ((0, "All"), (1, "Male"), (2, "Female"))


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="recipe_post", default=0)
    IRB_number = models.CharField(max_length=200, default=101)
    prin_invest = models.CharField(max_length=200, default='name')
    contact_name = models.CharField(
        max_length=400, unique=False, default='name')
    contact_email = models.CharField(
        max_length=200, unique=False, default='null')
    primary_disease = models.CharField(max_length=5000, blank=True)
    eligible_age_min = models.IntegerField(blank=False, default=0)
    eligible_age_max = models.IntegerField(blank=False, default=100)
    gender = models.IntegerField(choices=GENDER, default=0)
    main_image = CloudinaryField('image', default='placeholder')
    content = models.CharField(max_length=5000, blank=True)
    no_participants = models.ManyToManyField(
        User, related_name='ct_no_participants', blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    start_dt = models.DateField(default='2022-09-22')
    end_dt = models.DateField(default='2022-09-22')
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)
    # tag = models.ManyToManyField(Tags, related_name='tags', blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def no_enrolled(self):
        return self.no_participants.count()


class Question(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="questions")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Question {self.body} by {self.name}"


# class Tags(models.Model):
#     name = models.CharField(max_length=80, unique=True)

#     class Meta:
#         ordering = ["name"]

#     def __str__(self):
#         return self.name
