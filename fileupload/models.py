from django.db import models

class DataEntry(models.Model):
    name = models.CharField(max_length=100)
    value = models.FloatField()
    date = models.DateField()

    class Meta:
        db_table = 'data_entry'

    def __str__(self):
        return self.name
