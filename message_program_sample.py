import paho.mqtt.client as mqtt
import threading
import time
import string
import random
import json


class MessageProgram:

    def __init__(self, broker_ip: str, broker_port: int):
        # Template
        self.id = "client01"

        self.broker_ip = broker_ip
        self.broker_port = broker_port

        self.mqtt_client = mqtt.Client(self.id)
        self.mqtt_client.connect(self.broker_ip, self.broker_port)

        self.local_input_listener = LocalInputListener(self.mqtt_client, self.id)
        self.local_input_listener.start()

        self.message_listener = MessageListener(self.mqtt_client, self.id)


class LocalInputListener(threading.Thread):

    def __init__(self, mqtt_client, my_id):
        threading.Thread.__init__(self)
        self.mqtt_client = mqtt_client
        self.id = my_id

    def run(self):
        while True:
            user_input = input()
            session_id = user_input
            if " " in user_input:
                user_input_split_list = user_input.split(" ")
                session_id = user_input_split_list[0]

            # Template
            if session_id == "session_id_1":
                self.publish_message("server", session_id)
            elif session_id == "session_id_2":
                self.publish_message("server", session_id, user_input_split_list[1])
            elif session_id == "session_id_3":
                self.publish_message("client02", session_id)
            elif session_id == "session_id_4":
                self.publish_message("client02", session_id, user_input_split_list[1])
            elif session_id == "response_for":
                self.pub


            time.sleep(0.1)

    def publish_message(self, to, session_id, data=None):
        transaction_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=16))
        if data is not None:
            self.mqtt_client.publish(to + "/" + self.id + "/" + session_id + "/" + transaction_id, data)
        else:
            self.mqtt_client.publish(to + "/" + self.id + "/" + session_id + "/" + transaction_id)
        return True


class MessageListener:

    def __init__(self, mqtt_client, my_id):
        self.mqtt_client = mqtt_client
        self.id = my_id

        self.initialize_subscription()

    def initialize_subscription(self):

        def on_message(client, userdata, msg):
            topic_split_list = str(msg.topic).split("/")
            msg_to = topic_split_list[0]
            msg_from = topic_split_list[1]
            msg_session_id = topic_split_list[2]
            msg_transaction_id = topic_split_list[3]
            print(f" $$${msg_from} $$${msg_session_id} $$${msg_transaction_id} $$${msg.payload.decode()}")

            # Template
            if msg_transaction_id == "":


        print("Subscribed: ", self.id)
        self.mqtt_client.subscribe(self.id + "/#")
        self.mqtt_client.on_message = on_message

        self.mqtt_client.loop_start()


# Template
message_program = MessageProgram("18.117.19.11", 1883)


