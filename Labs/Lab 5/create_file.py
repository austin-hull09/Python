
def create_file(file_name, n):
    x = 0
    for i in range(n):
        x += 1
        file_name.write(str(x))
        file_name.write("\n")

output = open("file.out", "w")

create_file(output, 100)

output.close()
