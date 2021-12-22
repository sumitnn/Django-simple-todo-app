from django.db import models
from django.contrib.auth.models import User


class TODO(models.Model):
    status_choices = [
        ('C', 'Completed'),
        ('P', 'Pending'),
    ]
    priority_choices = [
        (1, ' 1️⃣'),
        (2, '2️⃣'),
        (3, '3️⃣'),
        (4, '4️⃣'),
        (5, '5️⃣'),
        (6, '6️⃣'),
        (7, '7️⃣'),
        (8, '8️⃣'),
        (9, '9️⃣'),
        (10, '🔟'),
    ]

    title = models.CharField(max_length=50)
    status = models.CharField(max_length=2, choices=status_choices)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    priority = models.IntegerField(choices=priority_choices, default=1)


class Addpost(models.Model):
    event_name = models.CharField(max_length=30)
    data = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=30)
    image = models.ImageField(upload_to='event_img/')
    is_liked = models.BooleanField(default=False)
    is_comnt = models.BooleanField(default=False)
