import random
import string

# Set number of words to generate
num_words = 300000000

# Generate a list of random words of the desired size
alphanum_and_special = string.ascii_letters + string.digits + string.punctuation

# Open the file for writing in binary mode
with open("300000000_words.txt", "wb") as file:
    for i in range(num_words//1000):
        random_words = [''.join(random.choice(alphanum_and_special) for _ in range(random.randint(1, 7))) for _ in range(1000)]
        # Join the words into a single string separated by newlines
        random_string = " ".join(random_words)
        # Insert new lines at random intervals
        new_lines = [i for i in range(0, len(random_string), random.randint(100, 500))]
        for i in new_lines:
            random_string = random_string[:i] + "\n" + random_string[i:]
        # Write the string to the text file
        file.write(random_string.encode())
        
    # handle remaining words
    if num_words % 1000:
        random_words = [''.join(random.choice(alphanum_and_special) for _ in range(random.randint(1, 7))) for _ in range(num_words % 1000)]
        # Join the words into a single string separated by newlines
        random_string = " ".join(random_words)
        # Insert new lines at random intervals
        new_lines = [i for i in range(0, len(random_string), random.randint(100, 500))]
        for i in new_lines:
            random_string = random_string[:i] + "\n" + random_string[i:]
        # Write the string to the text file
        file.write(random_string.encode())

    
print("Done!!!")