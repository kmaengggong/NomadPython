# BLUEPRINT | DONT EDIT

import requests
from bs4 import BeautifulSoup

response = requests.get(
    "https://berlinstartupjobs.com/engineering/",
    headers={
        "User-Agent":
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    })

skills = ["python", "typescript", "javascript", "rust"]

# /BLUEPRINT

# 👇🏻 YOUR CODE 👇🏻:

'''
https://berlinstartupjobs.com/engineering/
https://berlinstartupjobs.com/skill-areas/python/
https://berlinstartupjobs.com/skill-areas/typescript/
https://berlinstartupjobs.com/skill-areas/javascript/
첫 번째 URL에는 페이지가 있으므로 pagination 을 처리해야 합니다.
나머지 URL은 특정 스킬에 대한 것입니다. URL의 구조에 스킬 이름이 있으므로 모든 스킬을 스크래핑할 수 있는 스크래퍼를 만드세요.
회사 이름, 직무 제목, 설명 및 직무 링크를 추출하세요.
'''

# 0. 변수 및 상수 선언
BASE_URL = "https://berlinstartupjobs.com"
results = {}

# 1. 함수 선언
def scrape_page(sub_url, page=None, skill=None):
    result = []
    
    url = f"{BASE_URL}/{sub_url}"
    if page is not None:
        url = f"{url}/page/{page}"
    if skill is not None:
        url = f"{url}/{skill}"
    response = requests.get(
        url,
        headers={
            "User-Agent":
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
    )
    
    soup = BeautifulSoup(response.content, "html.parser")
    jobs = soup.find("ul", class_="jobs-list-items").find_all("li", class_="bjs-jlid")
    for job in jobs:
        company_name = job.find("a", class_="bjs-jlid__b").text
        job_title = job.find("h4", class_="bjs-jlid__h").find("a").text
        job_description = job.find("div", class_="bjs-jlid__description").text
        job_link = job.find("h4", class_="bjs-jlid__h").find("a")["href"]
        result.append({
            "company_name": company_name,
            "job_title": job_title,
            "job_description": job_description,
            "job_link": job_link
        })
        
    return result

# 2. 엔지니어링 URL 페이지 확인
soup = BeautifulSoup(response.content, "html.parser")
buttons = soup.find("ul", class_="bsj-nav").find_all("a", class_="page-numbers")
total_pages = int(buttons[-2].text)

# 2-1. 엔지니어링 URL 스크래핑
engineering_results = []
for page in range(1, total_pages + 1):
    engineering_result = scrape_page(sub_url="engineering", page=page)
    engineering_results.append(engineering_result)

results['engineering'] = engineering_results

# 3. 스킬 URL 스크래핑
for skill in skills:
    skill_result = scrape_page(sub_url="skill-areas", skill=skill)
    results[skill] = skill_result

# 4. 출력
for key, values in results.items():
    print(f"{key}:\n")
    print(values)
    print("-"*50)
    
# /YOUR CODE