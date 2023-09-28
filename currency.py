#Steve
#23.09.28
money = int(input('whats the money?'))
print(f'{money} can be made with:')
left = 0
for a in (100, 50, 20, 10, 5, 1, 0.25, 0.1, 0.05, 0.01):
    print(f'{money//a} a dollar bill(s)')
    money = money%a