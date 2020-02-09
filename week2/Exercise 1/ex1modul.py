import os
import csv

def print_file_content(file):
    with open(file) as file_object:
        contents = file_object.read()
    print(contents)




def write_list_to_file(output_file, touples):
    with open(output_file, 'w') as file_object:
        for x in touples:
            file_object.write(x + '\n')
            


def write_list_to_file(output_file, string):
     with open(output_file, 'w') as file_object:
            for x in string:
                file_object.write(x + '\n')


                
def read_csv(input_file):
    with open(input_file) as file_object:
        csvfile = []
        read = csv.reader(file_object)
        for r in read:
            csvfile.append(r)
        return read
        
