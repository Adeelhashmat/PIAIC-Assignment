

def star_border_decorator(func):
    """Decorator to wrap the message in a starry galaxy border."""
    def wrapper(message):
        border = "✨" * (len(message) + 8)
        decorated = f"{border}\n🌠  {message}  🌠\n{border}"
        return decorated
    return wrapper

def alien_emojis_decorator(func):
    """Decorator to add alien emojis around the message."""
    def wrapper(message):
        result = func(message)
        return f"👽🛸 {result} 🛸👽"
    return wrapper
