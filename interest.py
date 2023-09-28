#Steve
#23.09.27
P = int(input("P"))
n = int(input('n'))
r = 0.01*int(input('rate'))
t = int(input('time'))
print(P*(1+r/n)**(n*t))