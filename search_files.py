import os
import re
import argparse
from termcolor import colored


def generate_regex(pattern):
    # Split the input pattern into individual words
    words = pattern.split()

    # Rejoin the words with '\s+' to allow for one or more whitespace characters
    regex_pattern = r'.*'.join(map(re.escape, words))
    regex_pattern = r'.*' + regex_pattern + r'.*'
    print(regex_pattern)

    return regex_pattern


def search_directory(pattern, directory, extension):
    regex_pattern = generate_regex(pattern)
    findings = []

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    lines = f.readlines()
                for i, line in enumerate(lines):
                    match = re.search(regex_pattern, line)
                    if match:
                        # print(match.start())
                        colored_match = colored(match.group(0), 'red')
                        colored_file = colored(file_path, 'magenta')
                        colored_line = line[:match.start()] + colored_match + line[match.end():]
                        colored_line_num = colored(i+1, 'blue')
                        findings.append(f"{colored_file}: {colored_line_num} - Match: {colored_line.strip()}")

    return findings


def main():
    parser = argparse.ArgumentParser(description="Search a directory for a regex pattern while ignoring whitespace.")
    parser.add_argument("-p","--pattern", help="The regex pattern to search for, with or without whitespace.")
    parser.add_argument("-d", "--directory", help="The directory to search in.")
    parser.add_argument("-e", "--extension", help="The file extension to be searched.")
    args = parser.parse_args()

    pattern = args.pattern
    directory = args.directory
    ext = args.extension
    # print(pattern, directory, ext)

    if not os.path.isdir(directory):
        print(f"Error: {directory} is not a valid directory.")
        return
    # print(pattern)
    findings = search_directory(pattern, directory, ext)

    if not findings:
        print("No matches found.")
    else:
        for finding in findings:
            print(finding)

if __name__ == "__main__":
    main()
