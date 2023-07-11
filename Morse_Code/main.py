morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
    'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...',
    'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.',
    ')': '-.--.-',
    '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '@': '.--.-.', ' ': '/'
}


def encode(word_to_encode: str):
    encoded_word = ""
    for char in word_to_encode:
        if char in morse_code and char != " ":
            encoded_word += morse_code[char] + ' '
        elif char == " ":
            encoded_word += "/ "
    return encoded_word


def decode(word_to_decode: str):
    decoded_chars = []
    morse_code_inverse = {v: k for k, v in morse_code.items()}

    for char in word_to_decode.split():
        decoded_char = morse_code_inverse.get(char)
        if decoded_char is not None:
            decoded_chars.append(decoded_char)

    decoded_word = ''.join(decoded_chars).capitalize()
    return decoded_word


def morse_code_converter():
    decoding = True
    print("Welcome to The Morse Encoder and Decoder")
    while decoding:
        option = input("What do you want to do today? Encode or Decode, Type A or B: ").upper()
        if option == "A":
            string_to_encode = input("Enter the word that you want to encode: ").upper()
            coded_text = encode(string_to_encode)
            print(f"The the encoded text is : {coded_text}")
        elif option == "B":
            string_to_decode = input("Enter the word you would like to decode: ").upper()
            decoded_text = decode(string_to_decode)
            print(f"The decoded text is: {decoded_text}")
        else:
            print("You have entered an invalid option try again.")
            morse_code_converter()

        if input(
                "Are you done with the Morse Code Converter? Enter any character to 'try again' or 'exit' to stop :") != 'exit':
            morse_code_converter()
        else:
            print("Thanks for using Morse Encoder and Decoder")
            decoding = False


morse_code_converter()
