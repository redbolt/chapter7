from os import listdir

def run(*args):
	print("[*] LISR DIR \n")
	files = listdir('.')
	return(str(files))

