def enigma_light():
# Create keys string
    keys = 'abcdefghijklmnopqrstuvwxyz !'
# Autogenerate the values string by offsetting original string
    values = keys [-1] + keys [0 : -1]
    #print(keys)
    #print(values)
# Create two dictionaries
    dict_encryption = dict(zip(keys, values))
    dict_decryption = dict(zip(values, keys))
# Or create 1 dictionary and then flip
    #dict_encryption = dict(zip(keys, values))
    #dict_decryption = {value : key for key, value in dict_encryption.items()}
# User input 'The message' and mode
    message = input('Enter your secret message quietly: ')
    mode = input('Crypto mode: encode (e) OR decrypt as default: ')
# Run encode or decode
    if mode.lower() == 'e':
        new_message = ''.join([dict_encryption[letter] for letter in message.lower()])
    else:
        new_message = ''.join([dict_decryption[letter] for letter in message.lower()])
# Return result
    return new_message.capitalize()

print(enigma_light())

