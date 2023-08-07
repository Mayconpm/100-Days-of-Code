import art

alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]


def caesar(direction, text, shift):
    max_index = len(alphabet)
    new_text = ""
    if direction == "decode":
        shift *= -1
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift
            new_position %= max_index
            shited_letter = alphabet[new_position]
        else:
            shited_letter = char
        new_text += shited_letter
    print(f"The {direction}d text is {new_text}")
    return new_text


print(art.logo)

caesar_continue = True
while caesar_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(direction, text, shift)
    go_again = input(
        """Type 'yes' if you want to go again.Otherwise type 'no'.\n"""
    ).lower()
    if go_again == "no":
        caesar_continue = False
