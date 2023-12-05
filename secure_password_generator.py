import secrets
import string

def generate_password(length):
	characters = string.ascii_letters + string.digits + string.punctuation
	password = ''.join(secrets.choice(characters) for _ in range(length))
	return password

passlen = int(input("Enter the length of the password: "))
secure_password = generate_password(passlen)
print(secure_password)
