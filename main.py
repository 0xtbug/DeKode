import re
import base64
import zlib
from art import *
from tqdm import tqdm

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def write_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)

def remove_pattern(content, pattern):
    return re.sub(pattern, '', content)

def extract_encoded_string(content):
    match = re.search(r"b'([^']+)'", content)
    if match:
        return match.group(1)
    return None

def decode_string(encoded_string, option):
    decoders = {
        1: lambda x: base64.b16decode(x[::-1]),
        2: lambda x: base64.b32decode(x[::-1]),
        3: lambda x: base64.b64decode(x[::-1]),
        4: lambda x: zlib.decompress(base64.b16decode(x[::-1])),
        5: lambda x: zlib.decompress(base64.b32decode(x[::-1])),
        6: lambda x: zlib.decompress(base64.b64decode(x[::-1])),
    }
    try:
        return decoders[option](encoded_string.encode('utf-8'))
    except Exception as e:
        raise ValueError(f"Decoding failed: {e}")

def get_pattern_to_remove(option):
    patterns = {
        1: r"_ = lambda __ : __import__\('base64'\)\.b16decode\(__\[\::-1\]\);",
        2: r"_ = lambda __ : __import__\('base64'\)\.b32decode\(__\[\::-1\]\);",
        3: r"_ = lambda __ : __import__\('base64'\)\.b64decode\(__\[\::-1\]\);",
        4: r"_ = lambda __ : __import__\('zlib'\)\.decompress\(__import__\('base64'\)\.b16decode\(__\[\::-1\]\)\);",
        5: r"_ = lambda __ : __import__\('zlib'\)\.decompress\(__import__\('base64'\)\.b32decode\(__\[\::-1\]\)\);",
        6: r"_ = lambda __ : __import__\('zlib'\)\.decompress\(__import__\('base64'\)\.b64decode\(__\[\::-1\]\)\);",
    }
    return patterns.get(option)

def display_menu():
    tprint("DeKode")
    print("Author: 0xtbug")
    print("Github: https://github.com/0xtbug\n")
    print("Select the encoding type:")
    print("1: base64.b16decode(__[::-1])")
    print("2: base64.b32decode(__[::-1])")
    print("3: base64.b64decode(__[::-1])")
    print("4: zlib.decompress(base64.b16decode(__[::-1]))")
    print("5: zlib.decompress(base64.b32decode(__[::-1]))")
    print("6: zlib.decompress(base64.b64decode(__[::-1]))")
    print("7: Exit")

def main():
    while True:
        try:
            display_menu()
            option = int(input("Enter your choice (1-7): "))
            
            if option not in range(1, 7) and option != 7:
                print("Invalid option. Please choose a number between 1 and 7.")
                continue
            elif option == 7:
                print("Exiting...")
                exit(0)

            decode_count = 0

            with tqdm(total=100, desc="Decoding progress", leave=False) as pbar:
                while True:
                    content = read_file('encode.txt')

                    pattern_to_remove = get_pattern_to_remove(option)
                    content = remove_pattern(content, pattern_to_remove)

                    encoded_string = extract_encoded_string(content)
                    if not encoded_string:
                        write_file('result.txt', content)
                        print("\n")
                        print(f"Successfully decoded the string {decode_count} time(s)!")
                        print("The decoded string is saved in result.txt")
                        return

                    write_file('temp.txt', encoded_string)
                    encoded_string = read_file('temp.txt')
                    decoded_string = decode_string(encoded_string, option)
                    write_file('encode.txt', decoded_string.decode('utf-8'))

                    decode_count += 1

                    pbar.update(10)

        except Exception as e:
            print(f"Error occurred: {e}")
            break

if __name__ == "__main__":
    main()
