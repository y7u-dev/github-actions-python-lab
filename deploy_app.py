import os

secret = os.environ.get('SECRET_MESSAGE')
print(f"Secret: {secret}")