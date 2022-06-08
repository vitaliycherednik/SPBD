from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
import Crypto.Hash.SHA512
from Crypto.Cipher import AES


def rsa_sign(plain_text, key, hash_algorithm=Crypto.Hash.SHA512):
    signer = PKCS1_v1_5.new(RSA.importKey(key))
    hash_value = hash_algorithm.new(plain_text)
    return signer.sign(hash_value)


def rsa_verify(sign, plain_text, key, hash_algorithm=Crypto.Hash.SHA512):
    hash_value = hash_algorithm.new(plain_text)
    verifier = PKCS1_v1_5.new(RSA.importKey(key))
    return verifier.verify(hash_value, sign)


def keys_rsa():
    private_key = RSA.generate(1024)
    public_key = private_key.publickey()
    with open("private.pem", "w") as prv_file:
        print("{}".format(private_key.exportKey()), file=prv_file)

    with open("public.pem", "w") as pub_file:
        print("{}".format(public_key.exportKey()), file=pub_file)
    return private_key, public_key


def main():
    while True:
        print('Choose a mode: \n'
              '1)signature + cipher text - 1\n'
              '2)decrypt - 2')
        try:
            a = int(input())
            if a == 1:
                private_key, public_key = keys_rsa()
                message = str(input('Input your message: '))
                signature = rsa_sign(message.encode(encoding='utf-8'), private_key.exportKey(format='PEM'))
                obj1 = AES.new('This is a key123'.encode("utf8"), AES.MODE_CBC, 'This is an IV456'.encode("utf8"))
                cipher_text = obj1.encrypt(message.encode('utf-8'))
                obj2 = AES.new('This is a key123'.encode("utf8"), AES.MODE_CBC, 'This is an IV456'.encode("utf8"))
                if rsa_verify(signature, message.encode('utf-8'), public_key.exportKey(format='PEM')) == True:
                    print('Signature verified!')
                else:
                    print('Could not verify the message signature.')
                print("Signature: ", signature)
                print("Cipher text: ", cipher_text)
            elif a == 2:
                obj1 = AES.new('This is a key123'.encode("utf8"), AES.MODE_CBC, 'This is an IV456'.encode("utf8"))
                cipher_text = obj1.encrypt(message.encode('utf-8'))
                obj2 = AES.new('This is a key123'.encode("utf8"), AES.MODE_CBC, 'This is an IV456'.encode("utf8"))
                print("Decrypted text: ", str(obj2.decrypt(cipher_text).decode('utf-8')))
        except:
            print('Error occurred')

if __name__ == '__main__':
    main()
