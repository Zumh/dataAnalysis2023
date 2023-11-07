#!/usr/bin/env python3

def file_extensions(filename):
    # traverse each line and split them with . delimeter
    # then assign the dictionary base on file name and file extension
    file_with_extension = {}
    file_no_extension = []
    with open(filename, "r") as files:

        for file in files:
            file = file.strip()
            try:
                
                file_name, file_extension = file.rsplit('.', 1)
                file_extension = file_extension.strip()
                if file_extension not in file_with_extension:
                    file_with_extension[file_extension] = []
                file_with_extension[file_extension].append(file)
            except ValueError:
                file_no_extension.append(file)
    return (file_no_extension, file_with_extension)

def main():
    no_extension, with_extension = file_extensions("src/filenames.txt")
    print(f"{len(no_extension)} files with no extension")
    for file_extension, file_name in with_extension.items():
        print(f"{file_name} {len(file_name)}")
if __name__ == "__main__":
    main()
