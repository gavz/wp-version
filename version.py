import requests
from bs4 import BeautifulSoup
import bcolors
import sys, argparse

def banner():
    print("""

            ░██╗░░░░░░░██╗██████╗░░░░░░░██╗░░░██╗███████╗██████╗░░██████╗██╗░█████╗░███╗░░██╗
            ░██║░░██╗░░██║██╔══██╗░░░░░░██║░░░██║██╔════╝██╔══██╗██╔════╝██║██╔══██╗████╗░██║
            ░╚██╗████╗██╔╝██████╔╝█████╗╚██╗░██╔╝█████╗░░██████╔╝╚█████╗░██║██║░░██║██╔██╗██║
            ░░████╔═████║░██╔═══╝░╚════╝░╚████╔╝░██╔══╝░░██╔══██╗░╚═══██╗██║██║░░██║██║╚████║
            ░░╚██╔╝░╚██╔╝░██║░░░░░░░░░░░░░╚██╔╝░░███████╗██║░░██║██████╔╝██║╚█████╔╝██║░╚███║
            ░░░╚═╝░░░╚═╝░░╚═╝░░░░░░░░░░░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═════╝░╚═╝░╚════╝░╚═╝░░╚══╝
                                                                                   Code by NG          
          """)

if len(sys.argv) > 1:
    banner()
    if (sys.argv[1] == '-u'):
        try:
            input_url = sys.argv[2]
            input_code = requests.get(input_url)

            parser = argparse.ArgumentParser()
            parser.add_argument("-u", required=True)
            args = parser.parse_args()

            soup = BeautifulSoup(input_code.text,'html.parser')
            try:
                input_find = soup.find(attrs={"name":"generator"})
                print(bcolors.BLUE + input_find['content'])
            except:
                print(bcolors.OKMSG + "Version not detected")
        except:
            print(bcolors.ERRMSG + 'Please enter python version.py -u <valid URL with http:// or https://> ')

    elif ((sys.argv[1] == '-h') | (sys.argv[1] == '--help')):
        print(bcolors.BOLD + 'usage: version.py [-h] -u URL' '\n' 'OPTIONS:' '\n' '-h,--help    '
                            'show this help message and exit' '\n''-u URL of wordpress website,   --url URL')
else:
    banner()
    print(bcolors.ERR + 'Please select atleast 1 option from (-u) or -h, with a valid domain name')


