import urllib.request
import urllib.parse
import re
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("-u", "--url", help = "URL input")

args = parser.parse_args()

if args.url:
    
    url= args.url
    resp = urllib.request.urlopen(url)
    rdata = resp.read()
    comments = re.findall(r'<!--(.*?)-->',str(rdata))
    for c in comments:
        print(c)
    