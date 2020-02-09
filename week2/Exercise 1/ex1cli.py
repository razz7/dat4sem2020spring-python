import sys
import getopt




def usage():
    return 'Usage : you can write to .csv files '


def run(arguments):
    try:
        opts, args = getopt.getopt(arguments, "ho:v", ["help", "output="])
    except getopt.GetoptError as err:
        print(err) 
        usage()
        sys.exit(2)

    output = None
    verbose = False
    for option, argument in opts:
        print(option)
        if option == "-v":
            verbose = True
        elif option in ("-h", "--help"):
            print(usage())
            sys.exit()
        else:
            assert False, "unhandled option"

    print(output)


if __name__ == "__main__" :
    run(sys.argv[1:])
