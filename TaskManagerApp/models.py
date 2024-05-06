from django.db import models
from django.utils import timezone

class Task(models.Model):
    title = models.CharField(max_length=200, default="")
    text = models.CharField(max_length=500, default="")
    creation_date = models.DateTimeField("creation date", default=timezone.now)
    due_date = models.DateTimeField("due date", null=True)
    is_done = models.BooleanField(default=False)
    def __str__(self):
        return """
task title: {}
task text: {}
is done: {}
""".format(self.title, self.text, self.is_done)
