'''
Get's the file's name from the user
'''
def get_file_name() -> str:
	filename = ''
	while filename == '':
		filename = input("Please enter the name of the Python file you wish to obfuscate: ")
	return filename

'''
Opens the file the use wants and returns a 
string(?) of all the contents of that file
'''
def get_file_contents(filename:str) -> str: # What type does it return?
	program = ''
	with open(filename) as f:
		for line in f.readlines():
			program += line
	return program

if __name__ == '__main__':
	filename = get_file_name()
	file_contents = get_file_contents(filename)
	print(file_contents)
