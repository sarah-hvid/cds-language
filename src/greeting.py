import argparse

def hello(name): # prints my name
    print(f"Hello, my name is {name}!")
    
def tell_age(age): # prints my age
    print(f"I am {age} years old.")

def parse_args():
    # Initialise argparse
    ap = argparse.ArgumentParser()
    # command line parameters
    ap.add_argument("-n", "--name", required = True, help = "The user name to print")
    ap.add_argument("-a", "--age", required = False, help = "The user age to print")
    # parse arguments
    args = vars(ap.parse_args())
    #return list of arguments
    return args
    

def main(): # defines the way I want the script to run
    #get arguments
    args = parse_args()
    hello(args["name"])
    tell_age(args["age"])
    
# if namespace variable is "__main__"
#translation: when this script is executed from the command line, do the following
if __name__ == "__main__":
    main()