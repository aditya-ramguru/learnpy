import art

print(art.logo)

letters = ([chr(i) for i in range(97, 123)])
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(plain_text, shift):
    encoded_text = ''
    for i in plain_text:
        ind = letters.index(i)
        index_after_shift = ind + shift
        if index_after_shift > 25:
            index_of_encoded = index_after_shift - 26
            encoded_text += letters[index_of_encoded]
        else:
            encoded_text += letters[index_after_shift]
    print(f"The encoded text is {encoded_text}.")


def decrypt(encoded_text, shift_amount):
    decoded_text = ''
    for alphabet in encoded_text:
        ind = letters.index(alphabet)
        index_after_shift = ind - shift_amount
        if index_after_shift < 0:
            index_of_decoded = index_after_shift + 26
            decoded_text += letters[index_of_decoded]
        else:
            decoded_text += letters[index_after_shift]
    print(f"The decoded text is {decoded_text}.")

while input("Do you want to run caesar cipher? Type yes or no: ") == 'yes':
    if direction == "encode":
        encrypt(text, shift)
    else:
        decrypt(text, shift)
