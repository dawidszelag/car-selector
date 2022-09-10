from django.db import models


class UploadDataInfo(models.Model):
    class Status(models.IntegerChoices):
        FINISH = 1
        PROCESSING = 2
        ERROR = 3

    all_items = models.PositiveSmallIntegerField(default=0)
    current_item = models.PositiveSmallIntegerField(default=0)
    message = models.CharField(max_length=300)
    status = models.PositiveSmallIntegerField(null=True, choices=Status.choices)
