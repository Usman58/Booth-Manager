from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import json

STATUS_CHOICES = (
      ('Available', 'Available'),
      ('Occupied', 'Occupied'),
      ('Closed', 'Closed'),
  )
class Booth(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    status= models.CharField( max_length = 50,choices = STATUS_CHOICES)
    def __str__(self):
        return self.title
        
    @staticmethod
    def booth_datails(booth_id):
        instance=Booth.objects.get(id=booth_id)
        data={}
        data['id']=instance.id
        data['status']=instance.status
        return data

@receiver(post_save,sender=Booth)
def booth_status_handler(sender,instance,created,**kwargs):
    if not created:
        channel_layer=get_channel_layer()
        data={}
        data['id']=instance.id
        data['status']=instance.status
        print(data)
        async_to_sync(channel_layer.group_send)(
            'booth_%s' % instance.id,{
                'type':'booth_status',
                'value':json.dumps(data)
            }
        )



