def palindrome(input_string):
    input_string = input_string.lower()

    input_string = ''.join(e for e in input_string if e.isalnum())
    if input_string == input_string[::-1]:
        print("Palindrome")
    else:
        print("Bukan Palindrome")
input_string = input("Masukkan string: ")
palindrome(input_string)