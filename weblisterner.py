import requests
from colorama import Fore, Back, Style
import argparse

#Suppress Insecure Request Warning
requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning) 

burp_proxies = {'http':'http://127.0.0.1:8080', 'https':'http://127.0.0.1:8080'}

def format_text(title, item):
    cr = '\r\n'
    section_break = cr + '*' * 20 + cr
    item = str(item)
    text = Style.BRIGHT + Fore.RED + title + Fore.BLACK + section_break + item + section_break
    return text


def main():
    if args.proxy.lower() == 'yes':
        r=requests.get(args.url, verify=False, proxies=burp_proxies)
    elif args.proxy.lower() == 'no':
        r=requests.get(args.url, verify=False)
    else:
        print('Wrong proxy argument used. Yes to use Burpsuite or No to send it directly.')
        exit()
    
    if not args.section:
        print(format_text('Status Code: ', r.status_code))
        print(format_text('Headers: ',r.headers))
        print(format_text('Cookies: ',r.cookies))
        print(format_text('Text: ',r.text))
    elif args.section == 'sc':
        print(format_text('Status Code: ', r.status_code))
    elif args.section == 'h':
        print(format_text('Headers: ',r.headers))
    elif args.section == 'c':
        print(format_text('Cookies: ',r.cookies))
    elif args.section == 'text':
        print(format_text('Text: ',r.text))
    else:
        print('Incorrect argument for --section. Please use \'sc\' for Status Code, \'h \' for headers, \'c\' for cookies, \'text\' for the main. Or no section argument will print out all sections.')




if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='OSWE Web Listerner for Burpsuite')
    parser.add_argument('--url', metavar='path', required=True, help='URL to test') #Need to check for correct URL
    parser.add_argument('--section', metavar='path', required=False, help='sc for Status Code, h for headers, c for cookies, text for the main') #Need to check for correct arguments
    parser.add_argument('--proxy', metavar='path', required=True, help='yes for Burpsuite, no for no proxy.')
    args = parser.parse_args()
    main()