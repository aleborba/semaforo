from Pubnub import Pubnub

publish_key = "pub-c-c446036d-8070-4a3e-aa0e-ed9eb2d2a7f1"
subscribe_key = "sub-c-f8f41034-3454-11e4-b3c3-02ee2ddab7fe"
secret_key = "sec-c-ZDQ0MmRkNWYtN2IwMS00NzU2LWFiYzAtNDEzZGM1NTNkZDRk"
cipher_key = ""
ssl_on = False

pubnub = Pubnub(publish_key=publish_key, subscribe_key=subscribe_key,
                secret_key=secret_key, cipher_key=cipher_key, ssl_on=ssl_on)

channel = "semaforo"
message = "{'amarelo': 'blink', 'verde': 'on', 'vermelho': 'off'}"

print pubnub.publish(channel, message)
