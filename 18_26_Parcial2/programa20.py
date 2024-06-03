num1 = {10, 5, 3, 2}
num2 = {4, 6, 1}
num3 = {20, 17, 9}



union = num1 | num2 | num3
print(union)

for pares in union:
    if pares % 2 == 0 : 
        print(pares)

