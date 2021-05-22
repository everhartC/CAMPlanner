from django.db import models
from loginReg.models import User
from django.urls import reverse

# Create your models here.
class Trip(models.Model):
    name = models.CharField(max_length=100)
    creator = models.ForeignKey(User, related_name="created_trips", on_delete=models.CASCADE)
    participants = models.ManyToManyField(User, related_name="users_on_trip")
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Trip Name: {self.name}"

class Gear(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.CASCADE)
    link = models.URLField()
    photo = models.ImageField(upload_to='images/')
    owner = models.ForeignKey(User, related_name='gear', on_delete=models.CASCADE)
    trips = models.ManyToManyField(Trip, related_name="gear_on_trip")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Gear: {self.name}"

    def get_absolute_url(self):
        return reverse("dashboard", args=[str(self.id)])


class Category(models.Model):
    name = models.CharField(max_length=200)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)

    def __str__(self):
        full_path = [self.name]
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent
        return ' -> '.join(full_path[::-1])

class Message(models.Model):
    msg = models.TextField()
    user_who_posted = models.ForeignKey(User, related_name="comment", on_delete=models.CASCADE)
    trip = models.ForeignKey(Trip, related_name="trip_comment", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)