import sys
import getopt
import ex1modul



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
        if option in ("-h", "--help"):
            print(usage())
            sys.exit()
               
    if len(args) > 1:
        response = ""
        for lines in ex1modul.read_csv(args[0]):
            response += s[0]
        
        ex1modul.write_list_to_file(args[1].split('=')[1], reaponse)
        sys.exit()
    else:
        print(ex1modul.read_csv(args[0]))
        sys.exit()

    print(output)


if __name__ == "__main__" :
    run(sys.argv[1:])
