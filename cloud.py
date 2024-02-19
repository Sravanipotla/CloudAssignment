# Importing necessary modules
import os
import socket
import string

# Setting path variables
base_directory = '/home/data'
output_directory = '/home/output'
# Accessing all files in the specified directory
files_in_directory = os.listdir("/home/data")

# Extracting text files
text_files = [file for file in files_in_directory if file.endswith('.txt')]

# Locating target files
if_file_path = os.path.join(base_directory, 'IF.txt')
limerick_file_path = os.path.join(base_directory, 'Limerick-1.txt')
result_file_path = os.path.join(output_directory, 'result.txt')

# Calculating the number of words in IF.txt
word_count_if = sum(len(row.split()) for row in open(if_file_path))

# Calculating the number of words in Limerick-1.txt
word_count_limerick = sum(len(row.split()) for row in open(limerick_file_path))

# Computing the top 3 most frequent words in IF.txt
word_frequency = {}
#with open(if_file_path) as if_file:
    #for line in if_file:
       # for word in line.split():
            #word = word.translate(str.maketrans('', '', string.punctuation))
            #word = word.capitalize()
            #word_frequency[word] = word_frequency.get(word, 0) + 1
with open(if_file_path) as if_file:
    for line in if_file:
        for word in line.split():
            # Remove punctuation and convert to lowercase
            word = word.translate(str.maketrans('', '', string.punctuation)).lower()
            if word in word_frequency:
                word_frequency[word] += 1
            else:
                word_frequency[word] = 1

# Sorting words by frequency in descending order
sorted_words = sorted(word_frequency.items(), key=lambda x: x[1], reverse=True)[:3]

# Getting the host machine's IP address
host_name = socket.gethostname()
ip_address = socket.gethostbyname(host_name)

# Writing output to the result.txt file
with open(result_file_path, 'w') as result_file:
    result_file.write("List of all text files in the directory:\n")
    for file in text_files:
        result_file.write(f"{file}\n")
    result_file.write(f"Number of words in Limerick.txt: {word_count_limerick}\n")
    result_file.write(f"Number of words in IF.txt: {word_count_if}\n")
    result_file.write(f"Total number of words in both files: {word_count_if + word_count_limerick}\n")
    result_file.write(f"Top 3 words with maximum number of counts in IF.txt:\n")
    for word, count in sorted_words:
        result_file.write(f"{word} -> count: {count}\n")
    
    result_file.write(f"IP address of the machine: {ip_address}\n")

# Displaying output from the result.txt file
with open(result_file_path) as result_file:
    for line in result_file:
        print(line)

