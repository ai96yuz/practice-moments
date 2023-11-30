import random
import string


def generate_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))


generated_password = generate_password(12)
print("Generated Password:", generated_password)
