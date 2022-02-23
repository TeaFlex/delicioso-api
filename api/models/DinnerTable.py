from django.db import models

class DinnerTable(models.Model):
    seats = models.IntegerField()

    @classmethod
    def does_table_exist(cls, table_id: int):
        return bool(cls.objects.filter(id=table_id)) 
    