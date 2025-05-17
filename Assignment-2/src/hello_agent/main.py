from message_formatter import leafy_border, butterfly_effect

@leafy_border
@butterfly_effect
def calm_greet(message):
    return message

if __name__ == "__main__":
    message = "Embrace the calm within 🌸"
    print(calm_greet(message))