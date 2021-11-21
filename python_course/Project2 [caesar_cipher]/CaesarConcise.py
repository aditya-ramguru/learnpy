import art

print(art.logo)

letters = ([chr(i) for i in range(97, 123)])


def caesar(start_text, shift_amount, cipher_direction):
    """"Encodes or decodes function based on cipher direction"""
    end_text = ''
    if cipher_direction == 'decode':
        shift_amount *= -1
    for i in start_text:
        if i in letters:
            ind = letters.index(i)
            index_after_shift = ind + shift_amount
            if index_after_shift > 25:
                index_after_shift = index_after_shift % 26
            if index_after_shift < 0:
                index_after_shift = (index_after_shift % 26) + 26
            end_text += letters[index_after_shift]
        else:
            end_text += i
    print(f"The {cipher_direction}d result : {end_text}")


while True:
    run = input("Do you want to run CAESARS CIPHER, Type 'yes' to run and no to exit: \n")
    if run == 'yes':
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        caesar(text, shift, direction)
    else:
        print("GOODBYE")
        break
