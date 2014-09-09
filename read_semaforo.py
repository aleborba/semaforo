from Pubnub import Pubnub
import json
import ast
import pingo

publish_key = "pub-c-c446036d-8070-4a3e-aa0e-ed9eb2d2a7f1"
subscribe_key = "sub-c-f8f41034-3454-11e4-b3c3-02ee2ddab7fe"
secret_key = "sec-c-ZDQ0MmRkNWYtN2IwMS00NzU2LWFiYzAtNDEzZGM1NTNkZDRk"
cipher_key = ""
ssl_on = False

pubnub = Pubnub(publish_key=publish_key, subscribe_key=subscribe_key,
                secret_key=secret_key, cipher_key=cipher_key, ssl_on=ssl_on)

channel = "semaforo"

def callback(message):
    status = ast.literal_eval(message)
    print status['amarelo']
    return True

pubnub.subscribe_sync(channel, callback=callback)
