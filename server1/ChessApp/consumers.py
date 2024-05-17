import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

class ChessConsumer(WebsocketConsumer):
    def connect(self):
        self.room_group_name = 'chess_game'

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()
    
    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        
        text_data_json = json.loads(text_data)
        row = text_data_json['row']
        column = text_data_json['column']

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'move_piece',
                'row': row,
                'column': column
            }
        )

    def send_positions(self, event):
        positions = event['positions']

        self.send(text_data=json.dumps({
            'type': 'positions',
            'positions': positions
        }))

    def move_piece(self, event):
        row = event['row']
        column = event['column']

        self.send(text_data=json.dumps({
            'type': 'move',
            'row': row,
            'column': column
        }))