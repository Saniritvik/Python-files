MORSE_TO_ENG = {'.-':'A', '-...':'B', '-.-.':'C', '-..':'D', '.':'E',
        '..-.':'F', '--.':'G', '....':'H', '..':'I', '.---':'J', '-.-':'K',
        '.-..':'L', '--':'M', '-.':'N', '---':'O', '.--.':'P', '--.-':'Q',
        '.-.':'R', '...':'S', '-':'T', '..-':'U', '...-':'V', '.--':'W',
            '-..-':'X', '-.--':'Y', '--..':'Z'}
    
ENG_TO_MORSE = {'A': '.-', 'B': '-...',
                'C': '-.-.', 'D': '-..', 'E': '.',
                'F': '..-.', 'G': '--.', 'H': '....',
                'I': '..', 'J': '.---', 'K': '-.-',
                'L': '.-..', 'M': '--', 'N': '-.',
                'O': '---', 'P': '.--.', 'Q': '--.-',
                'R': '.-.', 'S': '...', 'T': '-',
                'U': '..-', 'V': '...-', 'W': '.--',
                'X': '-..-', 'Y': '-.--', 'Z': '--..'}

def start(text, encrypt, MORSE_DICT):
    if encrypt:
        words_array = text.split(" ")
        final_sentence = []
        for i in words_array: 
            word = []
            capText=i.upper()
            for j in capText: 
                word.append(MORSE_DICT[j])
                word.append(" ")
                joined = ''.join(word)
            final_sentence.append(joined)
        print("Your sentence encrypted is:")
        return ''.join(final_sentence)
        
    else:
        words_array = text.split(" ")
        word = []
        for i in words_array: 
            word.append(MORSE_DICT[i])
        print("Your final sentence decrypted is:")
        return ''.join(word)

while True:
    user = input("Do you want to encrypt or decrypt? (E or D, press 1 to exit) ")

    if user.upper() == "E": 
        word = input("What word or phrase do you want to encrypt? ")
        output = start(word, True, ENG_TO_MORSE)
    
    if user.upper() == "D": 
        decrypt = input("What word or phrase do you want to decrypt? ")
        output = start(word, False, MORSE_TO_ENG)

    if user == "1": 
        print("Thank you for using this program!")
        break