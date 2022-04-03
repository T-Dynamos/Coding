def main():
	with open("pass.txt", 'rb') as file:
	           for line in file:
	               print(line)
	               for word in line.split():
	                   		print("\n")
pass
main()