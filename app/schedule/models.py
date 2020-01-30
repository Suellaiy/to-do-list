from django.db import models


class Schedule(models.Model):
    date_time = models.DateTimeField()
    context = models.TextField(max_length=300)
    complete_schedule = models.BooleanField(default=False)

