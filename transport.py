import sys 

def default():
	print("I take people from one place to another") 

if __name__ == "__main__":
	if sys.argv[1]=="train":
		print("I ply on the tracks.")
	elif sys.argv[1]=="IC814":
		print("I was hijacked from Kathmandu")
	else:
		default()

