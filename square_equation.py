import sys

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

# ax^2 + bx + c = 0

D = pow(b, 2) - 4 * a * c

if D > 0:
    x1 = (-b + pow(D, 0.5)) / (2 * a)
    x2 = (-b - pow(D, 0.5)) / (2 * a)
    print(str(int(x1)) + ', ' + str(int(x2)))
elif D == 0:
    x1 = -b / (2 * a)
    print(int(x1))
else:
    print('There are no roots on the set of real numbers.')
