#Steve
#23.09.28
money = float(input('whats the money?'))
print(f'{money} can be made with:')
left = 0
word = {100: 'hundred', 50: 'fifty', 20: 'twenty', 10: 'ten', 5: 'five', 1: 'one', 0.25: 'quarter', 0.1: 'dimes', 0.25: 'quarter', 0.05: 'nickel', 0.01: 'penny'}



for a in (100, 50, 20, 10, 5, 1, 0.25, 0.1, 0.05, 0.01):
    print(f'{money//a} {word[a]} dollar bill(s)')
    money = money%a