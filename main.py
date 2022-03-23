from keys import generate_keys
def main():
    primes = input("Enter to prime numbers, seperated by a space: (eg. 1721 2689): ")
    primes = primes.split(' ')

    keys = generate_keys(int(primes[0]), int(primes[1]))
    pub_key = keys[0]
    priv_key = keys[1]

    print(f""" GENERATED KEYS:
    public key: {pub_key},
    private key: {priv_key},
    """)

    text = input("Enter text to encrypt: ")

    cipherText = encrypt(priv=pub_key[0], pub=pub_key[1], text=text)

    print(f"Ciphertext: {cipherText}")

    decipherText = decrypt(priv=priv_key[0], pub=priv_key[1], text=cipherText)

    print(f"Deciphertext: {decipherText}")

def encrypt(priv, pub, text):
    return [pow(ord(c), priv, pub) for c in text]

def decrypt(priv, pub, text):
    return ''.join([chr(pow(c, priv, pub)) for c in text])

if __name__ == '__main__':
    main()