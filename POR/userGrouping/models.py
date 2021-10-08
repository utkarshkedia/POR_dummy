from django.db import models

# Create your models here.
class GPU(models.Model):
    name_of_the_gpu = models.CharField(max_length=100)
    memory_type = models.CharField(max_length=100)
    board_name = models.CharField(max_length=100)
    ROM_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name_of_the_gpu
