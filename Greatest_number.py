def myNum(self):
    max_value = num[-1]
    for i in range(input_no):
        if (num[i] >= max_value):
            max_value = num[i]
    return max_value
input_no = int(input("Enter no of input = "))
num = []
for i in range(input_no):
    num.append(int(input(f'Enter No {i} : ')))
print(f'The Greatest Number is : {myNum(num)}')
