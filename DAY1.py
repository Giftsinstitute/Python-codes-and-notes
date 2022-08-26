num1 = 68 #variable num1 holding an integer value of 68
num2 = 52.4 #variable num2 holding a floating value of 52.4
name = 'gift' # variable holding a string value of gift
X = True # variable X holding a boolean value True
print (num1)

word = 'we\'re brothers from the other side of the town' # backward slash denote escape character
print (word)

word2 = "we're brothers from the other side of the town"
print (word2)

word3 = 'python is fun, \npython is easy, \npython is an highlevel language' # backward slash + n (\n) denotes new line
print (word3)

word4 = ''' python is fun
python is easy
python is an highlevel language ''' # this is a multiline string
print (word4)

# STRING CONCATENATION
print ('hello' + ' ' +'world' ) #joining of string and string
print ( 'hello ' + 'world')

print ('welcome to python class ' + name) # joining of string and variable also holding a string value

surname = 'kanjuni'
print(surname, name) # joining of variable and variable holding string value

# STRING FORMATTING
price1 = 45000
price2 = 15000
price3 = 85000
report = ' I sold 3 shirts for {}, 2 pairs of shoes for {}, and a suit for {}'
print(report.format(price1,price2,price3))

print(f'I sold 3 pairs of shirt for {price1}, 2 pairs of shoe for {price2}, and a suit for {price3}')

