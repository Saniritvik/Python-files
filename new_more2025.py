def start():
     while True: 
          ## Prompt the user with the option to exit, encrypt, or decrypt
          user = input("Do you want to encrypt or decrypt? (E or D, type no to exit) ")

        ## Call the encrpytion sentence function to encrypt the user's message
          if user.upper() == "E":
               plain_text = input("What is the text you want to encrypt? ")
               encrypted_sentance=encryptSentence(plain_text)
               print("Your message has been encrypted:")
               print(f"{encrypted_sentance}")
          ## Call the decryption sentence function to decrypt the user's sentence
          if user.upper() == "D":
               cypher_text = input("What is the text you want to decrypt? ")
               decrypted_sentence = decryptSentence(cypher_text)
               print("Your message has been decrypted:")
               print(f"{decrypted_sentence}")
        ## Break out the loop and stop the code
          if user.upper() == "NO" or user == "No": 
               print("Thank you for using this program")
               break

def decryptWord(cypherText):
    ## Morse code dictionary keys are in morse, values are in English alphabet
    MORSE_TO_ENG = {'.-':'A', '-...':'B', '-.-.':'C', '-..':'D', '.':'E',
    '..-.':'F', '--.':'G', '....':'H', '..':'I', '.---':'J', '-.-':'K',
    '.-..':'L', '--':'M', '-.':'N', '---':'O', '.--.':'P', '--.-':'Q',
    '.-.':'R', '...':'S', '-':'T', '..-':'U', '...-':'V', '.--':'W',
        '-..-':'X', '-.--':'Y', '--..':'Z'}
    
    ## Splits the morse code text based on the spaces
    split_text=cypherText.split(" ")
    
    ## A list for the decrypted values to be appended to
    decrypted=[]
    
    ## Iterating for each word in split_text
    for i in split_text:
        decrypted.append(MORSE_TO_ENG[i]) # i is a key value in morse code relating to the dictionary
    return ''.join(decrypted) ## Returns the decrpytion as a string

def decryptSentence(encryptedSentence):
        ## Adding a space to the encrypted sentence
        encryptedSentence+= " "
        
        ## Decrypted sentence will be appended into this list 
        decrypted_sentence=[]
        
        ## Splitting 
        wordsArray=encryptedSentence.split(" ")
        
        for i in range(len(wordsArray)-1): ## Without the -1, it gives an error as it cannot go beyond its dictionary values
            decrypted_sentence.append(decryptWord(wordsArray[i])) ## Passing the morse code 
            decrypted_sentence.append(" ")
        return ''.join(decrypted_sentence)

def encryptWord(plainText): 
    ENG_TO_MORSE = {'A': '.-', 'B': '-...',
                'C': '-.-.', 'D': '-..', 'E': '.',
                'F': '..-.', 'G': '--.', 'H': '....',
                'I': '..', 'J': '.---', 'K': '-.-',
                'L': '.-..', 'M': '--', 'N': '-.',
                'O': '---', 'P': '.--.', 'Q': '--.-',
                'R': '.-.', 'S': '...', 'T': '-',
                'U': '..-', 'V': '...-', 'W': '.--',
                'X': '-..-', 'Y': '-.--', 'Z': '--..'}
    
    answer=[]
    capText=plainText.upper()
    for i in capText:
        answer.append(ENG_TO_MORSE[i])
        answer.append(" ")
    return ''.join(answer)

def encryptSentence(plainSentence): 
    encryptedWord=[]
    wordsArray=plainSentence.split(" ")
    for i in wordsArray:
        encryptedWord.append(encryptWord(i))
    return ''.join(encryptedWord)



start()