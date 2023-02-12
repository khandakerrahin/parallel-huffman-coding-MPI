import random
import string

# Define the size of the file in bytes
file_size_in_mb = 6.5
file_size = int(file_size_in_mb * 1024 * 1024)

# Define the characters to be used for the random text
chars = string.ascii_letters + string.digits + string.punctuation

# Write random characters to a file
with open(f"{file_size_in_mb}MB_text.txt", "w") as file:
    count = 0
    while count < file_size:
        line_size = random.randint(20, 1000)
        for i in range(line_size):
            if count >= file_size:
                break
            file.write(random.choice(chars))
            count += 1
            if (i + 1) % random.randint(7, 25) == 0 and count < file_size - 1:
                file.write(" ")
                count += 1
        if count >= file_size - 1:
            break
        file.write("\n")
        count += 1

# Trim the file if necessary
if count > file_size:
    with open(f"{file_size_in_mb}MB_text.txt", "rb+") as file:
        file.seek(file_size - 1)
        file.truncate()