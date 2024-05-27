import json
import os
from telethon import TelegramClient, events, types
from config import phone, api_id, api_hash

# Вставь сюда свои данные https://my.telegram.org/


# Загрузка сохраненного состояния
if os.path.exists('seen_users.json'):
    with open('seen_users.json', 'r') as file:
        seen_users = json.load(file)
else:
    seen_users = []

# Создание клиента
client = TelegramClient(phone, api_id, api_hash)

@client.on(events.NewMessage)
async def handler(event):
    sender = await event.get_sender()
    sender_id = sender.id

    # Проверка, является ли отправитель группой, каналом или ботом
    if isinstance(sender, types.User):
        if sender.bot:
            return
    elif isinstance(sender, (types.Chat, types.Channel)):
        return

    # Проверка, является ли сообщение из личного чата
    if event.is_private:
        if sender_id not in seen_users:
            # Отправка приветственного сообщения
            try:
                await event.reply('Привет! Спасибо за ваше сообщение.')

                # Добавление пользователя в список
                seen_users.append(sender_id)

                # Сохранение состояния
                with open('seen_users.json', 'w') as file:
                    json.dump(seen_users, file)
            except Exception as e:
                print(f"Error sending message to {sender_id}: {e}")

# Запуск клиента
with client:
    print("Client is running...")
    client.run_until_disconnected()
