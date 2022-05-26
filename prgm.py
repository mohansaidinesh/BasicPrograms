import streamlit as st
st.title(' Basic Programs')
st.subheader("One required Input's")
num = st.number_input("enter a number")
if st.button("square root"):
	sum = num**0.5
	st.write('square root is',sum)
if st.button('+ve / -ve'):
	if num>0:
		st.write("Positive number")
	elif num==0:
		st.write("zero")
	else:
		st.write("Negative number")
if st.button('even / odd'):
	if num%2==0:
		st.write('even number')
	else:
		st.write('odd number')
if st.button("leap year"):
	if (num % 400 == 0) and (num % 100 == 0):
		st.write('leap year')
	elif (num % 4 ==0) and (num % 100 != 0):
		st.write('leap year')
	else:
		st.write('not a leap year')
if st.button("prime number"):
	nums = int(num)
	flag = False
	if nums > 1:
    		for i in range(2,nums):
        		if (nums % i) == 0:
            			flag = True
            			break
	if flag:
    		st.write("not a prime number")
	else:
    		st.write("prime number")
if st.button("factorial"):
	nums = int(num)
	factorial = 1
	if num < 0:
   		st.write("Sorry, factorial does not exist for negative numbers")
	elif num == 0:
   		print("The factorial of 0 is 1")
	else:
   		for i in range(1,nums + 1):
       			factorial = factorial*i
   		st.write("The factorial of",nums,"is",factorial)
if st.button("table"):
	for i in range(1, 11):
   		st.write(num, 'x', i, '=', num*i)
if st.button('fibanocci sequence'):
	nterms = int(num)
	n1, n2 = 0, 1
	count = 0
	if nterms <= 0:
   		st.write("Please enter a positive integer")
	elif nterms == 1:
   		st.write(n1)
	else:
   		while count < nterms:
       			st.write(n1)
       			nth = n1 + n2
       			n1 = n2
       			n2 = nth
       			count += 1
if st.button('Armstong'):
	nums = int(num)
	order = len(str(nums))
	sum = 0
	temp = num
	while temp > 0:
   		digit = temp % 10
   		sum += digit ** order
   		temp //= 10
	if num == sum:
   		st.write(num,"is an Armstrong number")
	else:
   		st.write(num,"is not an Armstrong number")
if st.button("Dec to others"):
	nums = int(num)
	st.write(bin(nums), "in binary.")
	st.write(oct(nums), "in octal.")
	st.write(hex(nums), "in hexadecimal.")
if st.button("Factors "):
	x = int(num)
	for i in range(1, x + 1):
		if x % i == 0:
			st.write(i)
if st.button('Reverse'):
	nums = int(num)
	reversed_num = 0
	while nums != 0:
    		digit = nums % 10
    		reversed_num = reversed_num * 10 + digit
    		nums //= 10
	st.write(reversed_num)
if st.button('No.of Digits'):
	st.write(len(str(int(num))))
if st.button('area of circle'):
	r = int(num)
	PI = 3.142
	st.write(PI * (r*r))
if st.button('fibonacci'):
	n = int(num)
	a = 0
	b = 1
	if n < 0:
		st.write("Incorrect input")
	elif n == 0:
		st.write(a)
	elif n == 1:
		st.write(b)
	else:
		for i in range(2, n):
			c = a + b
			a = b
			b = c
		st.write(b)
if st.button('Palindrome'):
	number = int(num)
	reverse = 0
	temp = number
	while(temp > 0):
    		Reminder = temp % 10
    		reverse = (reverse * 10) + Reminder
    		temp = temp //10
	if(number == reverse):
    		st.write("Palindrome number")
	else:
    		st.write("Not a Palindrome number")
if st.button('Perfect number'):
	Number = int(num)
	Sum = 0
	for i in range(1, Number):
    		if(Number % i == 0):
        		Sum = Sum + i
	if (Sum == Number):
    		st.write("Perfect Number")
	else:
    		st.write("Not a Perfect Number")
if st.button('Power of 2'):
	n = int(num)
	if n&n-1 ==0:
		st.write('Power of two')
	else:
		st.write('Not Power of two')
st.subheader("Two required Input's")
num_1 = st.number_input('enter first number')
num_2 = st.number_input('enter second number')
if st.button("add"):
	sum = num_1+num_2
	st.write('addition of two numbers is',sum)
if st.button("subtract"):
	sub = num_1-num_2
	st.write('subtraction of two numbers is',sub)
if st.button("multiply"):
	sum = num_1*num_2
	st.write('multiplication of two numbers is',sum)
if st.button("division"):
	sum = num_1/num_2
	st.write('division of two numbers is',sum)
if st.button("remainder"):
	sum = num_1%num_2
	st.write('remainder of two numbers is',sum)
if st.button("Armstrong Intervel"):
	lower = int(num_1)
	upper = int(num_2)
	for num in range(lower, upper + 1):
   		order = len(str(num))
   		sum = 0
   		temp = num
   		while temp > 0:
       			digit = temp % 10
       			sum += digit ** order
       			temp //= 10
   		if num == sum:
       			st.write(num)
if st.button('HCF'):
	x = int(num_1)
	y = int(num_2)
	while(y):
       		x, y = y, x % y
	st.write('HCF is ',x)
if st.button('LCM'):
	x = int(num_1)
	y = int(num_2)
	if x > y:
		greater = x
	else:
		greater = y
	while(True):
		if((greater % x == 0) and (greater % y == 0)):
			lcm = greater
			break
		greater += 1
	st.write('LCM is',lcm)
if st.button('Power'):
	base = int(num_1)
	exponent = int(num_2)
	result = 1
	for exponent in range(exponent, 0, -1):
    		result *= base
	st.write(result)
if st.button('Prime Intervel'):
	x = int(num_1)
	y = int(num_2)
	for i in range(x, y):
		if i == 0 or i == 1:
			continue
		else:
			for j in range(2, int(i/2)+1):
				if i % j == 0:
					break
			else:
				st.write(i)
st.subheader("Three required Input's")
num1 = st.number_input('enter 1st number')
num2 = st.number_input('enter 2nd number')
num3 = st.number_input('enter 3rd number')
if st.button('area of triangle'):
	if (num1<0 or num2<0 or num3<0):
		st.write("side of triangle can't be negative")
	else :
		s = (num1+num2+num3)/2
		area = (s*(s-num1)*(s-num2)*(s-num3)) ** 0.5
		st.write('area of triangle',area)
if st.button('maximum'):
	if (num1 >= num2) and (num1 >= num3):
   		largest = num1
	elif (num2 >= num1) and (num2 >= num3):
   		largest = num2
	else:
   		largest = num3
	st.write('largest is ',largest)