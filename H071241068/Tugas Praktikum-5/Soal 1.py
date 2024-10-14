def main(a):

    b = a.lower()
    d = b.replace(" ", "")
    c = (''.join(reversed(d)))
  

    if c == d:
        print('Polindrome')
    else:
        print('Not Polindrome')
    
main(input('Masukkan kata:'))