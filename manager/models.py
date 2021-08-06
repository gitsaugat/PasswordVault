from django.db import models
import uuid
from django.contrib.auth.models import User
from django.db.models.fields.json import JSONField
# Create your models here.

class Password(models.Model):
    uid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        help_text="Password ID"
    )
    user = models.ForeignKey(User , on_delete=models.CASCADE , null=False , blank=False , related_name="Data_User")
    title = models.CharField(default = "" ,max_length=400 , null=False , blank=False)
    datas = JSONField(
        null = True ,
        blank = True,
        default = dict
    )
    data_note = models.TextField(null=True,blank=True)

    date_added  = models.DateTimeField(auto_now_add=True , null=True , blank=True)

    def __str__(self) -> str:
        return str(self.uid)