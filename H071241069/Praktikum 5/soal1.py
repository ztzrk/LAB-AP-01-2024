kata = input("Masukkan kata: ").lower()
kata = kata.replace(" ", "")
if kata == kata[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")