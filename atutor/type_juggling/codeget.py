import hashlib
import string
import itertools
import re
import sys
import argparse

'''
Function to generate email address that can produce 
MD5 hash vaule of 0eXXXXX where X is numerical value
 '''

def gen_code(email_domain, user_id, date_value, prefix_length):
    if prefix_length is None:
        print("Prefix length is required.")
        return []

    if not isinstance(prefix_length, int):
        print("Prefix length must be an integer.")
        return []

    results = []
    match_pattern = f'^0[eE]\d+$'
    possible_emails = map(''.join, itertools.product(string.ascii_lowercase, repeat=prefix_length))
    for email in possible_emails:
        hash_string = f'{email}@{email_domain}{date_value}{user_id}'.encode('utf-8')
        hash_value = hashlib.md5(hash_string).hexdigest()[:10]
        # print(hash_value)
        if re.match(match_pattern, hash_value):
            results.append(f'{email}@{email_domain}')
            # print(hash_string, hash_value)
    return results

def main():
    parser = argparse.ArgumentParser(description='Generate email address that will give 0eNNNNN MD5 hash result.')
    parser.add_argument('-d', '--domain', type=str, help='Email Domain')
    parser.add_argument('-D', '--date', type=str, help='Creation Date')
    parser.add_argument('-l', '--length', type=int, help='Prefix Length')
    parser.add_argument('-i', '--id', type=int, help='User ID')

    args = parser.parse_args()

    results = gen_code(args.domain, args.id, args.date, args.length)
    if results:
        for idx, result in enumerate(results, start=1):
            print(f'{idx}. Found email address that can work: {result}')
        

if __name__ == '__main__':
    main()
    



