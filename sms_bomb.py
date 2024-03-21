import requests

def send_sms(target_number, message, num_messages):
    for _ in range(num_messages):
        requests.post("https://api.example.com/send-sms", data={"number": target_number, "message": message})
        # Burada "https://api.example.com/send-sms" yerine gerçek bir SMS API'sinin URL'sini kullanmalısın.

target_number = "hedef_telefon_numarasi"  # Hedef telefon numarası buraya yazılmalı.
message = "Merhaba! Bu bir test mesajıdır."  # Gönderilecek mesajı buraya yazabilirsin.
num_messages = 100  # Kaç tane SMS göndermek istediğini buradan ayarlayabilirsin.

send_sms(target_number, message, num_messages)
