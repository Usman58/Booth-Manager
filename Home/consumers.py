from channels.generic.websocket import WebsocketConsumer
import json
from .models import Booth
from asgiref.sync import async_to_sync


class MyConsumer(WebsocketConsumer):

    def connect(self):
        self.room_name=self.scope['url_route']['kwargs']['booth_id']
        print(self.room_name, self.channel_name)
        self.room_group_name='booth_%s' % self.room_name
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()
        booth=Booth.booth_datails(self.room_name)
        print(booth)
        self.send(text_data=json.dumps({'payload':booth}))

        
        

    def receive(self, text_data):
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type':'booth_status',
                'payload':text_data
            }
        )
        

    def disconnect(self, *args, **kwargs):
         async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def booth_status(self, e):
        print(e, 'statussss')
        booth=json.loads(e['value'])
        self.send(text_data=json.dumps({'payload':booth}))
