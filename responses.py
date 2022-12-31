import random


def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return 'Hey there'

    if p_message == 'roll':
        return str(random.randint(1,10))
    
    if p_message == 'help':
        return "'This is a help message that you can modify'"

    return "I don't understand what you said can you repeat yourself"