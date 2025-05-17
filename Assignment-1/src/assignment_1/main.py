# main.py

from assignment_1.message_formatter import star_border_decorator, alien_emojis_decorator

@alien_emojis_decorator
@star_border_decorator
def display_message(msg):
    return msg

if __name__ == "__main__":
    message = "Exploring the universe, one star at a time!"
    print(display_message(message))
