from django.db import models

class Task(models.Model):
    STATUS_CHOICES = [
        ('CREATED', 'Vytvořen'),
        ('IN_PROGRESS', 'Probíhá'),
        ('COMPLETED', 'Dokončen'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='CREATED')

    def __str__(self):
        return self.title
