from django.db import models
from django.urls import reverse
from django.utils import timezone



class NGO(models.Model):
    name = models.CharField(max_length=200, verbose_name="NGO Name")
    registration_number = models.CharField(max_length=100, unique=True)
    contact_person = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    website = models.URLField(blank=True, null=True)
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "NGO"
        verbose_name_plural = "NGOs"
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ngo_detail', kwargs={'pk': self.pk})

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date_time = models.DateTimeField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    location_details = models.TextField(blank=True, help_text="Additional location details")
    ngo = models.ForeignKey(NGO, on_delete=models.CASCADE, related_name='events')
    poster = models.ImageField(upload_to='event_posters/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_time']

    def __str__(self):
        return f"{self.title} - {self.ngo.name}"

    def get_absolute_url(self):
        return reverse('event_detail', kwargs={'pk': self.pk})

    @property
    def is_upcoming(self):
        return self.date_time > timezone.now()

    @property
    def location(self):
        return f"{self.city}, {self.state}"