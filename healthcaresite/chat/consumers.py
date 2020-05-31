from channels.auth import channel_session_user
from channels import Group
from channels.generic.websocket import WebsocketConsumer
import json

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        self.send(text_data=json.dumps({
            'message': message
        }))

# @channel_session_user
# def ws_connect(message):
#     Group('cold-homeTherapy').add(message.reply_channel)

#     message.channel_session['cough-homeTherapy'] = 'cold-homeTherapy'

#     message.reply_channel.send({
#         'accept': True
#     })


# @channel_session_user
# def ws_disconnect(message):
#     user_group = message.channel_session['cough-homeTherapy']

#     Group(user_group).discard(message.reply_channel)


# @channel_session_user
# def ws_recieve(message):
#     data = json.loads(message.content.get('text'))

#     if data.get('cures') == 'cold':
#         Group('cold-homeTherapy').add(message.reply_channel)
#         Group('cough-homeTherapy').discard(message.reply_channel)

#         message.channel_session['cure-group'] = 'cold-homeTherapy'

#     elif data.get('cures') == 'cough':
#         Group('cough-homeTherapy').add(message.reply_channel)
#         Group('cold-homeTherapy').discard(message.reply_channel)

#         message.channel_session['cure-group'] = 'cough-homeTherapy'
