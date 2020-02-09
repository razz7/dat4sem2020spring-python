import os


def filepathtofolder(folder, output):
    with open(output, 'w') as File:
        for folders in os.listdir(folder):
            File.write(folder + folders + "\n")


def filepathWritenames(folder, output):
    with open(output, 'w') as File:
        for path, directories, files in os.walk(folder):
            for filenames in files:
                File.write(os.path.join(path, filenames) + "\n")

def print_first_file_line(filename):
    for l in filename:
            with open(l, 'r') as File:
                print(File.readline())
