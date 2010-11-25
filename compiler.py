input_file="dr"

current_file = open(input_file)

a_file_that = current_file.read()

print(a_file_that)

a_file_that.readline(2)

def print_a_line(line_count, f):
        print (line_count, f.readline())
