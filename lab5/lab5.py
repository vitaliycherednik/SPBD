import rsa

def generate_keys():
    (publicKey, privateKey) = rsa.newkeys(1024)
    with open('keys/publickey.pem', 'wb') as f:
        f.write(publicKey.save_pkcs1('PEM'))

    with open('keys/privatekey.pem', 'wb') as f:
        f.write(privateKey.save_pkcs1('PEM'))


def load_keys():
    with open('keys/publickey.pem', 'rb') as f:
        publicKey = rsa.PublicKey.load_pkcs1(f.read())

    with open('keys/privatekey.pem', 'rb') as f:
        privateKey = rsa.PrivateKey.load_pkcs1(f.read())

    return publicKey, privateKey


def encrypt(message, key):
    return rsa.encrypt(message.encode('ascii'), key)


def decrypt(cipher, key):
    try:
        return rsa.decrypt(cipher, key).decode('ascii')
    except:
        return False


def sign_sha1(message, key):
    return rsa.sign(message.encode('ascii'), key, 'SHA-1')


def verify_sha1(message, signature, key):
    try:
        return rsa.verify(message.encode('ascii'), signature, key) == 'SHA-1'
    except:
        return False

generate_keys()
publicKey, privateKey = load_keys()

message = input('Enter a message:')
cipher_text = encrypt(message, publicKey)

signature = sign_sha1(message, privateKey)

plain_text = decrypt(cipher_text, privateKey)

print(f'Cipher text: {cipher_text}')
print(f'Signature: {signature}')

if plain_text:
    print(f'Plain text: {plain_text}')
else:
    print('Could not decrypt the message.')

if verify_sha1(plain_text, signature, publicKey):
    print('Signature verified!')
else:
    print('Could not verify the message signature.')
