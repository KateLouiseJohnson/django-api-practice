from django.db import models

class Data(models.Model):
    attributeOne = models.CharField(max_length=200)
    attributeTwo = models.CharField(max_length=200)
    attributeThree = models.CharField(max_length=200)

    def __str__(self):
        return 'This row contains: ' + str(self.attributeOne)
