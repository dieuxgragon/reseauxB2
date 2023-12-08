import __future__
import argparse
import requests
import os

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--url", action="store")
argv = parser.parse_args()
print (argv.url)

def get_content(url):
    r = requests.get(url)
    return (r.text)
    
def write_content(content, file):
    working_directory = os.getcwd()
    f=open(working_directory+file,"w", encoding="utf-8")
    f.write(content)
    f.close()


write_content(get_content(argv.url),"\\tmp\web_page")