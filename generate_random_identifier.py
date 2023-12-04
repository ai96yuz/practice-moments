import secrets
import string


def generate_random_identifier(length=10):
    characters = string.ascii_letters + string.digits
    random_identifier = ''.join(secrets.choice(characters) for _ in range(length))
    return random_identifier


new_identifier = generate_random_identifier(16)
print("Generated Identifier:", new_identifier)
