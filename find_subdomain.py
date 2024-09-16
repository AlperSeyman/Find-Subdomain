import requests

#target_url = input("Enter your target website url: ")
target_url = "google.com"


def make_reqeust(url):
    try:
        return requests.get(url)    
    except requests.exceptions.ConnectionError:
        print(f"Did not find subdomain -----> {url}")

with open("Find-Subdomain/subdomainlist.txt","r") as subdomainlist:
    for word in subdomainlist:
        word = word.strip()
        url= "http://"+ word + "." + target_url
        response = make_reqeust(url)
        if response:  # if response is not None
            print(f"Found subdomain -----> {url}")