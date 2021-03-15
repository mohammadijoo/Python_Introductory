import os

def main():
    
    print(os.name)             # getting operating system name
    print(os.getenv('PATH'))   # getting environment variables
    print(os.getcwd())         # getting current directory
    print(os.urandom(15))      # getting random bytes with long of 15

if __name__ == "__main__":
    main()




    
