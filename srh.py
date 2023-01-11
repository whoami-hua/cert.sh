import argparse
import requests
from lxml import etree

def banner():
    print(""""
                       __           __
       ________  _ ___/ /_    _____/ /_
      / ___/ _ \/ v__/ __/   ( _-</ __ \
     / /__/  __/ /  / /_ _    _) / / / /
     \___/\___/_/   \__/(_)/___(/_/ /_/ --@whoami
    """)

print(banner())
parser = argparse.ArgumentParser()
parser.add_argument( "-t","--query",help="search term (required)" )
parser.add_argument( "-v","--version",help="version information" )

parser.parse_args()
args = parser.parse_args()

def search(query):

    url = 'https://crt.sh/?'
    header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36'}
    date = {
        'q':query
    }
    reque = requests.get(url=url,params=date,headers=header)
    html = reque.text


    return html

def regular(string):

    item = []
    pars_html = etree.HTML(string)
    dd_list = pars_html.xpath("//tr/td[6]/text()")
    for dd in dd_list:
        string = dd
        new_string = string.replace("*.", "")
        item.append(new_string)
    return item

def deal_with(string):
    valuse = list(set(string))

    num_values = len(valuse)
    for dd in valuse:
        print(dd)

    print('Catch '+ str(num_values) + ' Subdomains, the program is finished')


if __name__ == '__main__':

    sc = search(args.query)
    bt = regular(sc)
    deal_with(bt)

