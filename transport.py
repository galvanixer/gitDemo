import sys 

def default():
	print("I take people from one place to another") 

if __name__ == "__main__":
	if sys.argv[1]=="train":
		print("I ply on the tracks.")
	else:
		default()

