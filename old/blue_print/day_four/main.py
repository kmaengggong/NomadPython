import os
import requests
import validators  # use for domains (.com, .co.kr, .net, .org, etc.)

def isItDown():
  print("Welcome to IsItDown.py!")
  print("Please write a URL or URLs you want to check. (separated by comma)")
  given_urls = input()
    
  # 1. get clean urls from given_urls
  temp_urls = []
  temp_urls = given_urls.split(',')
  urls = []
  for url in temp_urls:
    urls.append(url.strip().lower())
    
  # 2. check each url
  for url in urls:
    # remove "http://" for url valid check
    if url[0:7] == "http://":
      url = url[7:]
    # url valid check
    if not validators.domain(url):
      print(url, "is not a valid URL.")
    else:
      # append "http://""
      if url[0:7] != "http://":
        url = "http://" + url
      # check url is up or down
      try:
        req = requests.get(url)
        if req.status_code == requests.codes.ok:
          print(url, "is up!")
      except:
        print(url, "is down!")

def main():
  cont = 'y'
  # cotniue loop if answer is not 'n' and 'N'
  while (cont != 'n') and (cont != 'N'):
    if (cont == 'y') or (cont == 'Y'):
      os.system("clear")
      isItDown()
    else:
      print("That's not a valid answer")
    cont = str(input("Do you want to start over? y/n "))
  print("k. bye!")

if __name__ == '__main__':
  main()

# hello.com -> http://hello.com is up!
# http://goole.com -> http://google.com is up!
# youTUBE.COM -> http://youtube.com is up!
# google.com,    youtube.com, redditttttt.com -> up, up, down
# gggggggg -> gggggggg is not a valid URL.
# asdf -> That's not a valid answer
# n -> k. bye!