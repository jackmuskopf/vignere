import string
import random
import argparse

# # hardcode these to ensure static ordering
# known_characters = string.ascii_letters + string.digits + string.punctuation + ' \n\t'
known_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%&'()*+,-./:;<=>?@[\]^_`{|}~ \t\n"

def new_key(length=30):

    # star with an empty key
    key = ""

    # add a random char to the key up to the length
    for i in range(length):
        key += random.choice(string.ascii_letters)
    
    # return the key that we created
    return key

def encrypt(message, key):

    # start with empty encrypted message
    encrypted_message = ""

    # for each character in the message, rotate it using the key
    for index, message_character in enumerate(message):
        
        # skip any characters we don't recognize
        if message_character not in known_characters:
            encrypted_message += message_character
            continue

        # get key character corresponding to this message character
        key_index = index % len(key)

        # get the key char for this character of the message
        key_char = args.key[key_index]

        # get the distance to rotate as an integer
        rotation_distance = string.ascii_letters.index(key_char)

        # get the index of the encrypted character
        encrypted_character_index = (known_characters.index(message_character) + rotation_distance) % len(known_characters)

        # add the encrypted character to the encrypted message
        encrypted_message += known_characters[encrypted_character_index]
    
    # all done!
    return encrypted_message

def decrypt(message, key):

    # start with empty encrypted message
    decrypted_message = ""

    # for each character in the message, rotate it using the key
    for index, encrypted_character in enumerate(message):
        
        # skip any characters we don't recognize
        if encrypted_character not in known_characters:
            decrypted_message += encrypted_character
            continue

        # get key character corresponding to this message character
        key_index = index % len(key)

        # get the key char for this character of the message
        key_char = args.key[key_index]

        # get the distance to rotate as an integer
        rotation_distance = string.ascii_letters.index(key_char)

        # get the index of the encrypted character
        decrypted_character_index = (known_characters.index(encrypted_character) - rotation_distance) % len(known_characters)

        # add the encrypted character to the encrypted message
        decrypted_message += known_characters[decrypted_character_index]
    
    # all done!
    return decrypted_message

if __name__ == '__main__':

    commands = ['create-key', 'encrypt', 'decrypt']

    parser = argparse.ArgumentParser(description='Encrypt and decrypt messages!')
    parser.add_argument('command', type=str,
                        help=f'the command; one of: {", ".join(commands)}')

    parser.add_argument('--key', type=str,
                        help=f'A key to use to encrypt or decrypt a message')

    parser.add_argument('--text', type=str,
                        help=f'Input text, encrypted or decrypted')

    parser.add_argument('--in-file', type=str,
                        help=f'A file with a message to encrypt or decrypt')

    parser.add_argument('--out-file', type=str,
                        help=f'A file to save the encrypted or decrypted message')

    args = parser.parse_args()

    # get input text (encrypted or decrypted)
    text = None
    if args.in_file:
        with open(args.in_file, 'r') as in_file:
            text = in_file.read()
    elif args.text:
        text = args.text

    # create a key
    if args.command == 'create-key':
        print(new_key())

    elif args.command == 'encrypt':
        result = encrypt(text, args.key)
        print(result)
        if args.out_file:
            with open(args.out_file, 'w') as out_file:
                out_file.write(result)

    elif args.command == 'decrypt':
        result = decrypt(text, args.key)
        print(result)
        if args.out_file:
            with open(args.out_file, 'w') as out_file:
                out_file.write(result)

    else:
        print(f'Invalid command: {args.command}; please use: {", ".join(commands)}')