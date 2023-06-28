MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..'}

morseDecrypt={'.-':'A', '-...':'B', '-.-.':'C', '-..':'D', '.':'E',
 '..-.':'F', '--.':'G', '....':'H', '..':'I', '.---':'J', '-.-':'K',
  '.-..':'L', '--':'M', '-.':'N', '---':'O', '.--.':'P', '--.-':'Q',
   '.-.':'R', '...':'S', '-':'T', '..-':'U', '...-':'V', '.--':'W',
    '-..-':'X', '-.--':'Y', '--..':'Z'}

## Makes morse code word into normal english
def decrpytWord(cypherText):
    someArray=cypherText.split(" ")
    answer=[]
    for i in someArray:
        answer.append(morseDecrypt[i])
    return ''.join(answer)

## Makes more code sentance into normal english
def decrpytSentance(encryptedSentance):
    encryptedSentance=encryptedSentance + " "
    decrytedWord=[]
    wordsArray=encryptedSentance.split(" ")
    for i in range(len(wordsArray)-1):
        decrytedWord.append(decrpytWord(wordsArray[i]))
        decrytedWord.append(" ")
    return ''.join(decrytedWord)

## Makes normal english word un-readable
def encrpytWord(plainText):
    answer=[]
    capText=plainText.upper()
    for i in capText:
        answer.append(MORSE_CODE_DICT[i])
        answer.append(" ")
    return ''.join(answer)

## Makes normal english sentance un-readable
def encrpytSentance(plainSentance):
    encrytedWord=[]
    wordsArray=plainSentance.split(" ")
    for i in wordsArray:
        encrytedWord.append(encrpytWord(i))
    return ''.join(encrytedWord)

inf=True

while inf:
    doe=input("Do you want to encrypt text or decrpyt text? (E or D or No)")
    
    if doe == "E":
        plainText=input("What is the text you want to encrypt")
        encryptedSentance=encrpytSentance(plainText)
        print("Your message has been encrypted:")
        print("---___--- ---___--- ---___--- ---___--- ---___--- ---___---")
        print(encryptedSentance)
        print("---___--- ---___--- ---___--- ---___--- ---___--- ---___---")

    if doe == "D":
        cypherText=input("What is the text you want to decrypt")
        decryptedSentance=decrpytSentance(cypherText)
        print("Your message has been decrypted:")
        print("---___--- ---___--- ---___--- ---___--- ---___--- ---___---")
        print(decryptedSentance)
        print("---___--- ---___--- ---___--- ---___--- ---___--- ---___---")
    
    if doe == "No":
        print("Stopping code")
        inf=False

