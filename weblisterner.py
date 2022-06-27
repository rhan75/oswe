import requests
from colorama import Fore, Back, Style
import argparse

requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

#proxies = {'http':'http://127.0.0.1:8080', 'https':'http://127.0.0.1:8080'}

def format_text(title, item):
    cr = '\r\n'
    section_break = cr + '*' * 20 + cr
    item = str(item)
    text = Style.BRIGHT + Fore.RED + title + Fore.BLACK + section_break + item + section_break
    return text

# r = requests.get('https://www.yahoo.com', verify=False, proxies=proxies)
# print(format_text('r.status_code is: ', r.status_code))
# print(format_text('r.headers is: ',r.headers))
# print(format_text('r.cookies is: ',r.cookies))
# print(format_text('r.text is: ',r.text))

def main():

    r=requests.get(args.url, verify=False)
    
    if not args.section:
        print(format_text('r.status_code is: ', r.status_code))
        print(format_text('r.headers is: ',r.headers))
        print(format_text('r.cookies is: ',r.cookies))
        print(format_text('r.text is: ',r.text))
    elif args.section == 'sc':
        print(format_text('r.status_code is: ', r.status_code))
    elif args.section == 'h':
        print(format_text('r.headers is: ',r.headers))
    elif args.section == 'c':
        print(format_text('r.cookies is: ',r.cookies))
    elif args.section == 'text':
        print(format_text('r.text is: ',r.text))
    else:
        print('Wrong section argument. Please use sc for Status Code, h for headers, c for cookies, text for the main. Or no section argument will print out all sections.')




if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='OSWE Web Listerner for Burpsuite')
    parser.add_argument('--url', metavar='path', required=True, help='URL to test') #Need to check for correct URL
    parser.add_argument('--section', metavar='path', required=False, help='sc for Status Code, h for headers, c for cookies, text for the main') #Need to check for correct arguments
    args = parser.parse_args()
    main()