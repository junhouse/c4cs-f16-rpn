import operator
from termcolor import colored, cprint

operators = {
	'+': operator.add,
	'-': operator.sub,
	'*': operator.mul,
	'/': operator.truediv,
	'^': operator.pow,
}

def calculate(myarg):
	stack = list()
	for token in myarg.split():
		try:
			token = int(token)
			stack.append(token)
		except ValueError:
			function = operators[token]
			arg2 = stack.pop()
			arg1 = stack.pop()
			result = function(arg1, arg2)
			stack.append(result)
		print(stack)
	if len(stack) != 1:
		raise TypeError("Too many parameters")
	return stack.pop()

def doSomething(sto):
	firstname = "Jun"
	lastname = "kim"
	fullname = firstname + lastname + sto
	print (fullname)

def main():
	while True:
		result = calculate(input("rpn calc> "))
		print ("Result: ")
		if result > 0:
			cprint(result, 'blue', attrs=['bold'])
		else:
			cprint(result, 'red', attrs=['bold'])

if __name__ == '__main__':
	main()
