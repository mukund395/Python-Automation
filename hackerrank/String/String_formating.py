n = 17
for i in range(1,n+1):
    print(f'{i:{len(bin(n)[2:])}}', f'{i:{len(bin(n)[2:])}o}', f'{i:{len(bin(n)[2:])}X}', f'{i:{len(bin(n)[2:])}b}')

