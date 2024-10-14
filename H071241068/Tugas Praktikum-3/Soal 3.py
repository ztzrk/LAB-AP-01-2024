# n = int(input(' N : ')) 
# m = int(input(' M : ')) 


# if n>=1 and m>=1:
#     for i in range(n):
#         if i % 2 == 0:  
#             for j in range(m):
#                 print(f"MOVE to ({i},{j})")
#         else:  
#             for j in range(m-1, -1, -1):
#                 print(f"MOVE to ({i},{j})")

# if n<=1 and m<=1:
#     for i in range(0, n, -1):
#         if i % 2 == 0:  
#             for j in range(0, m, -1):
#                 print(f"MOVE to ({i},{j})")
#         else:  
#             for j in range(m+1, +1, +1):
#                 print(f"MOVE to ({i},{j})")

n = int(input('N: ')) 
m = int(input('M: ')) 


n_step = 1 if n > 0 else -1
m_step = 1 if m > 0 else -1


for i in range(0, n, n_step):
    if (i // abs(n_step)) % 2 == 0:  
        for j in range(0, m, m_step):
            print(f"MOVE to ({i},{j})")
    else:  
        for j in range(m - m_step, -m_step, -m_step):
            print(f"MOVE to ({i},{j})")

