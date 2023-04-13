from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA256
from Crypto.Signature import pkcs1_15
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def generate_key_pair(key_size=16384):
    key = RSA.generate(key_size)
    sk = key.export_key(format='PEM')
    pk = key.publickey().export_key(format='PEM')
    return sk, pk

def encrypt(pk_receiver, message):
    cipher = PKCS1_OAEP.new(RSA.import_key(pk_receiver))
    ciphertext = cipher.encrypt(pad(message, cipher._max_encrypt_size()))
    return ciphertext

def decrypt(sk, ciphertext):
    cipher = PKCS1_OAEP.new(RSA.import_key(sk))
    message = unpad(cipher.decrypt(ciphertext), cipher._max_decrypt_size())
    return message

def generate_signature(sk, message):
    key = RSA.import_key(sk)
    h = SHA256.new(message)
    signature = pkcs1_15.new(key).sign(h)
    return signature

def verify_signature(pk, message, signature):
    key = RSA.import_key(pk)
    h = SHA256.new(message)
    try:
        pkcs1_15.new(key).verify(h, signature)
        return True
    except (ValueError, TypeError):
        return False

def generate_fingerprint(pk):
    pk = RSA.import_key(pk)
    pk_der = pk.export_key(format='DER')
    hasher = SHA256.new(pk_der)
    fingerprint = hasher.hexdigest()
    return fingerprint
