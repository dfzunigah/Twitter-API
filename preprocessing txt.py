#Daniel Zuñiga - 03/03/17 @ National University of Colombia

#If you stored your data (tweets) in a .txt format instead of a db this script allows you
#    to test if your data can be load using JSON module
import json
import os
import glob

#Split a large file in a series of files up to 30000 lines
def split_file(filepath, lines=30000):
    """Split a file based on a number of lines."""
    path, filename = os.path.split(filepath)
    # filename.split('.') would not work for filenames with more than one .
    basename, ext = os.path.splitext(filename)
    # open input file
    with open(filepath, 'r') as f_in:
        try:
            # open the first output file
            f_out = open(os.path.join(path, '{}_{}{}'.format(basename, 0, ext)), 'w')
            # loop over all lines in the input file, and number them
            for i, line in enumerate(f_in):
                # every time the current line number can be divided by the
                # wanted number of lines, close the output file and open a
                # new one
                if i % lines == 0:
                    f_out.close()
                    f_out = open(os.path.join(path, '{}_{}{}'.format(basename, i, ext)), 'w')
                # write the line to the output file
                f_out.write(line)
        finally:
            # close the last output file
            f_out.close()

#Remove empty/blank lines of the file
def remove_empty_lines(filename):
    if not os.path.isfile(filename):
        print("{} does not exist ".format(filename))
        return
    #Depending on your machine it'd be able to process big amounts of data
    #    in my case 146Mb or 150 millions bytes is the limit
    if (os.stat(filename).st_size < 150000000): #146MB
        with open(filename) as filehandle:
            lines = filehandle.readlines()

        with open(filename, 'w') as filehandle:
            lines = filter(lambda x: x.strip(), lines)
            filehandle.writelines(lines)
            print(filename, ": Job done!")
    else:
        #If the file is way to big, then it goes to this function.
        split_file(filename)

#Count the number of lines in a file
def how_many_lines(filename):
    if not os.path.isfile(filename):
        print("{} does not exist ".format(filename))
        return
    num_lines = sum(1 for line in open(filename))
    return num_lines

#Test if the lines can be load to using JSON module
def test_json(filename):
    lista = []
    if not os.path.isfile(filename):
        print("{} does not exist ".format(filename))
        return
    try:
        with open(filename,"r") as file:
            for line in file:
                tweet = json.loads(line)
                lista.append(tweet)
        print("JSON approved: {} tweets in {}".format(how_many_lines(filename), filename))
    except Exception as error:
        print("Nea, something went wrong!")
        print(error)

#Returns a list of files in the default folder
def list_files():
    default_folder = "C:\\Users\\Daniel\\Desktop\\"
    lista = glob.glob(default_folder + "*.txt")
    print ("Found {} files matching".format(len(lista)))
    return lista

#Implementation of all the functions
all_files = list_files()
for file in all_files:
    remove_empty_lines(file)
    test_json(file)
