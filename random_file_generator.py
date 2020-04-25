import os
from copy import deepcopy
import random
import string

# Generates a random file of random size, with random content, grouped by random words of random length.

def random_string(stringLength=200):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


def wordify(input):
    output = deepcopy(input)
    iter_factor = int(len(input) / 10)
    for _ in range(iter_factor):
        rand_index = random.randint(0, len(output) - 1)
        output = output[:rand_index] + ' ' + output[rand_index:]
    return output


def write_to_file(file_length):
    file_name = random_string(20)
    for line in range(file_length):
        with open(os.path.join(os.getcwd(), file_name + '.txt'), 'a') as my_random_file:
            my_random_file.write(wordify(random_string()) + os.linesep)


if __name__ == '__main__':
    write_to_file(random.randint(0, 3000))
