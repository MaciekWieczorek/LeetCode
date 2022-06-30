def reverse(x):
        minus = False
        if x > (-2)**(31) and x < (2)**(31)-1:
            y = str(x)
            if y[0] == "-":
                y = y[1:]
                minus = True
                
            y = y[::-1]
            integer = int(y)
            if minus == True:
                integer = integer * (-1)
            
            return integer
        else:
            return 0

print(reverse(1534236469))
print((2)**(31))