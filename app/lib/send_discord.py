import requests

def send_discord_message(webhook_url, message):
    payload = {'content': message}
    response = requests.post(webhook_url, json=payload)
    if response.status_code == 204:
        print('Message sent successfully.')
    else:
        print('Failed to send message.')
        print(response.text)