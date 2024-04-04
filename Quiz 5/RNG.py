import secrets
random_bytes = secrets.token_bytes(1048576)
with open("random.bin", "wb") as file:
    file.write(random_bytes)