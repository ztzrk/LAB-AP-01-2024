def generate_substrings(a):
    n = len(a)
    for start in range(n):  
        substring = ""  
        for end in range(start, n): 
            substring += a[end] 
            print(substring)  
generate_substrings(input("Input your string: "))
