def copy_file(infile, outfile):
    """Copies the content of infile to a new outfile"""
    with open(infile) as file:
        with open(outfile, 'w') as file_1:
            file_1.write(file.read())
copy_file('capitals.txt', 'new_capitals.txt')