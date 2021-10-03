from char_morse import morse


# ------------ Functions ------------- #
def to_morse(msg):
    morse_msg = ''
    morse_list = []
    for word in msg:
        for chara in word:
            if chara in morse:
                morse_char = morse[chara]
                morse_list.append(morse_char + ' ')
            elif chara == ' ':
                morse_list.append('| ')
            elif chara not in morse:
                morse_list.append(chara + ' ')
    print(f'{morse_msg.join(morse_list)}\n')


def to_english(msg):
    decrypt_msg = ''
    decrypt_chara = []
    split_message = msg.split(' ')
    for chara in split_message:
        if chara in morse.values():
            for letter in morse:
                if morse[letter] == chara:
                    decrypt_chara.append(letter)
        elif chara == '|':
            decrypt_chara.append(' ')
        else:
            decrypt_chara.append(chara)
    print(f'{decrypt_msg.join(decrypt_chara).lower()}\n')


# -------------- Run Script --------- #

print("########## GOOD OLD MORSE ##########\n"
      "Covent Text messages to Morse Code and Decrypt Morse Code\n"
      "Type Morse code using '.' and '-' seperating letters with spaces and words by '|'")
while True:
    user_input = input('What would you like to do???\nTo Encrypt (E)\n'
                       'To Decrypt (D)\n'
                       'To Quit (Q): ').upper()
    if user_input == 'E':
        message = input('Type your message: \n').upper()
        to_morse(message)
    elif user_input == 'D':
        message = input('Type your message: \n')
        to_english(message)
    elif user_input == 'Q':
        exit()
    else:
        print('Wrong Input!!')
