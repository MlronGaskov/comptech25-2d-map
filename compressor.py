import string

from classes.compression import compress_map
from classes.polygon import load


def compress_file(input_file: string, output_file):
    compress_map(load(input_file)).write_to_file(open(output_file, "w"))


if __name__ == '__main__':
    for i in range(13):
        compress_file(f"./map-examples/test{i}.txt", f"./compressed/test{i}.txt")
        print(i)
