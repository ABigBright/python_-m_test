print("%s" %__name__)
import sys

if "__main__" == __name__:
    print("__main__ is executed\r\n")
    print("argv[*] = %s\r\n" %sys.argv[0:])
