from django.db import models
from loginReg.models import User
from django.urls import reverse

# Create your models here.
class Trip(models.Model):
    name = models.CharField(max_length=100)
    creator = models.ForeignKey(User, related_name="created_trips", on_delete=models.CASCADE)
    participants = models.ManyToManyField(User, related_name="trips")
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"


class Gear(models.Model):
    
    CATEGORY_CHOICES = [
        ('Water', (
            ('filter', 'Filter'),
            ('water', 'Water'),
        )),
        ('Shelter', (
            ('tent', 'Tent'),
            ('tarp', 'Tarp/Rainfly'),
        )),
        ('Sleep', (
            ('bag', 'Sleeping Bag'),
            ('pad', 'Sleeping Pad'),
        )),
        ('Cooking', (
            ('stove', 'Stove'),
            ('fuel', 'Fuel'),
        )),
        ('food', 'Food'),
        ('Clothes', (
            ('pants', 'Pants'),
            ('shirt', 'Shirt'),
            ('jacket', 'Jacket'),
        )),
    ]

    name = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    link = models.URLField(null=True, blank=True)
    photo = models.ImageField(upload_to='images/', null=True, blank=True)
    owner = models.ForeignKey(User, related_name='my_gear', on_delete=models.CASCADE)
    trips = models.ManyToManyField(Trip, related_name="trip_gear")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"

class Message(models.Model):
    msg = models.TextField(blank=True, null=True)
    user_who_posted = models.ForeignKey(User, related_name="comment", on_delete=models.CASCADE)
    trip = models.ForeignKey(Trip, related_name="trip_comment", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str(self):
        return f"{self.msg}"