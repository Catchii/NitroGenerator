from dhooks import Webhook
import time

webhook = input("Input Your Discord Webhook! ")
hook = Webhook(webhook)
time.sleep(120)
hook.send("Im Alive!")