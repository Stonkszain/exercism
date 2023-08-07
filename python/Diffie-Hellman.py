import random

# generates a random integer greater than 1 and less than p
def private_key(p):
    return random.randint(2,p - 1)

# calculates the public key
def public_key(p, g, private):
    return (g ** private) % p

# uses public key and private key to decode the secret
def secret(p, public, private):
    return (public ** private) % p
