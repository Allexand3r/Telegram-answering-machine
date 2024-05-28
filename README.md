# Telegram Auto-Responder Bot

This is a Telegram bot built with Telethon that automatically responds to the first message from a new user. The bot does not respond to messages from groups, channels, or bots.

## Features

- Responds only to personal messages from users who write to you for the first time.
- Ignores messages from bots, groups, and channels.
- Saves the state of users who have received a response to prevent multiple replies.

## Prerequisites

- Python 3.7 or higher
- Telethon library

## Installation

1. Clone the repository:

    ```sh
    https://github.com/Allexand3r/Telegram-answering-machine.git
    cd telegram-auto-responder
    ```

2. Create and activate a virtual environment (optional but recommended):

    ```sh
    python -m venv venv
    call venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required libraries:

    ```sh
    pip install telethon
    ```

4. Replace the placeholders in the script with your own Telegram API credentials:

    ```python
    api_id = 'YOUR_API_ID'
    api_hash = 'YOUR_API_HASH'
    phone = 'YOUR_PHONE_NUMBER'
    session_name = 'session_name'
    ```

## Usage

1. Run the script:

    ```sh
    python main.py
    ```

2. The bot will start running and respond to the first message from new users with a greeting message.

## Code Explanation

The script works as follows:

1. **Imports necessary modules**: Imports `Telethon`, `os`, and `json` for Telegram client, file operations, and JSON handling.
2. **Sets up Telegram client**: Defines `api_id`, `api_hash`, `phone` for Telegram authentication.
3. **Loads saved state**: Loads the list of users who have already received a response from `seen_users.json`. Creates an empty list if the file does not exist.
4. **Creates the Telegram client**: Uses `TelegramClient` to create a client for interacting with the Telegram API.
5. **Handles new messages**: Uses the `@client.on(events.NewMessage)` decorator to define an asynchronous function `handler` that processes each new message:
    - Gets the sender of the message and their ID.
    - Checks that the sender is not a bot, group, or channel.
    - Checks that the message is a personal message (`event.is_private`).
    - Sends a greeting message to users who have not yet received one, adds their ID to the list, and updates `seen_users.json`.
6. **Runs the client**: The client starts and waits for new messages until disconnected.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
