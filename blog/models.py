from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0,"Draft"), (1,"Published"))
GENDER = ((0,"All"), (1,"Male"), (2,"Female"))

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    prin_invest = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recipe_post", default=0)
    eligible_age_min = models.IntegerField(blank=False, default=0)
    eligible_age_max = models.IntegerField(blank=False, default=100)
    irb_number= models.CharField(max_length=200, unique=True)
    contact_email = models.CharField(max_length=200, unique=True)
    gender = models.IntegerField(choices=GENDER, default=0)
    main_image = CloudinaryField('image', default='placeholder')
    excerpt = models.CharField(max_length=500, blank=True)
    content = models.TextField()
    no_participants = models.ManyToManyField(User, related_name='no_participants', blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)


    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"