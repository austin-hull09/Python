# --------------------------------------
# CSCI 127, Lab 7
# October 17, 2017
# Austin Hull
# --------------------------------------

def print_matrix(matrix, rows, columns, title):
    default = 0
    print(title)
    print()
    for row in range(rows):
        print_header(columns)
        for column in range(columns):
            value = matrix.get((row, column), 0)
            print("|" + '{:>3}'.format(str(value)), end ="")    
        print("|")
    print_header(columns)
    print()

def add_matrices(matrix1, matrix2, rows, columns):
    matrix3 = {}
    for row in range(rows):
        for column in range(columns):
            added_value = (matrix1.get((row,column), 0) + matrix2.get((row, column), 0 ))
            if added_value != 0:
                matrix3[(row, column)] = added_value
    return(matrix3)
    
# --------------------------------------
# Do not change anything below this line
# --------------------------------------

def print_header(columns):
    line = "+"
    for i in range(columns):
        line += "---+"
    print(line)

# --------------------------------------

def read_matrix(input_file):
    matrix = {}
    line = input_file.readline().split()
    while line[0] != "stop":
        row = int(line[0])
        column = int(line[1])
        value = int(line[2])
        matrix[(row, column)] = value
        line = input_file.readline().split()
    return matrix

# --------------------------------------

def main (file_name):
    input_file = open(file_name, "r")
    
    line = input_file.readline().split()
    rows = int(line[0])
    columns = int(line[1])

    matrix_1 = read_matrix(input_file)
    print_matrix(matrix_1, rows, columns, "Matrix 1")
    
    matrix_2 = read_matrix(input_file)
    print_matrix(matrix_2, rows, columns, "Matrix 2")

    matrix_3 = add_matrices(matrix_1, matrix_2, rows, columns)
    print_matrix(matrix_3, rows, columns, "Matrix 1 + Matrix 2")
    print("Matrix 3 =", matrix_3)

# --------------------------------------

main ("sparse-matrix.txt")
