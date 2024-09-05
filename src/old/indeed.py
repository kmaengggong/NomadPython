import requests
from bs4 import BeautifulSoup

LIMIT = 50
INDEED_URL = f"https://www.indeed.com/jobs?q=python&limit={LIMIT}"

def extract_indeed_pages():
  indeed_result = requests.get(INDEED_URL)
  indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")
  pagination = indeed_soup.find("div", {"class":"pagination"})
  links = pagination.find_all("a")
  pages = []
  
  for link in links:
    pages.append(link.string)
  
  pages = pages[:-1]
  last_page = int(pages[-1])

  return last_page

def extract_indeed_jobs(last_page):
  jobs = []
  result = requests.get(f"{INDEED_URL}&start={0*LIMIT}")
  for page in range(last_page):
    result = requests.get(f"{INDEED_URL}&start={0*LIMIT}")
    print(result.status_code)
  indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")
    
  return jobs