from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

"""
Do this when scraping a website to avoid getting blocked.

headers = {
      'User-Agent':
      'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
      'Accept':
      'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
      'Accept-Language': 'en-US,en;q=0.5',
}

response = requests.get(URL, headers=headers)
"""

# 변수 및 상수 선언
BERLIN_URL = "https://berlinstartupjobs.com/skill-areas"  # + /{keyword}
WEB3_C_URL = "https://web3.career"  # + /{keyword}-jobs
WEWORK_URL = "https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term="  # + {keyword}

headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept':
    'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
}

# 함수 선언
def scrape_berlin(keyword):
    result = []
    url = f"{BERLIN_URL}/{keyword}"
    response = requests.get(url, headers=headers)

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

def scrape_web3(keyword):
    result = []
    url = f"{WEB3_C_URL}/{keyword}-jobs"
    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.content, "html.parser")
    jobs = soup.find("table", class_="table table-borderless").find_all("tr", class_="table_row", attrs={'data-jobid': True})

    for job in jobs:
        company_name = job.find("td", class_="job-location-mobile").find("h3").text
        job_title = job.find("div", class_="job-title-mobile").find("h2", class_="my-primary").text
        job_description = ""
        descs = job.find_all("div")[-1].find_all("span")
        for desc in descs:
            job_description += desc.find("a").text + ", "
        job_description = job_description.rstrip(", ")
        job_link = job.find("div", class_="job-title-mobile").find("a")["href"]
        result.append({
            "company_name": company_name,
            "job_title": job_title,
            "job_description": job_description,
            "job_link": f"{WEB3_C_URL}/{job_link}"
        })

    return result

def scrape_wework(keyword):
    result = []
    url = f"{WEWORK_URL}{keyword}"
    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.content, "html.parser")
    jobss = soup.find_all("section", class_="jobs")
    jobs = []
    for job in jobss:
        all_li = job.find("ul").find_all("li")
        jobs.append([li for li in all_li if "view-all" not in li.get("class", [])])

    for job in jobs:
        for j in job:
            company_name = j.find_all("span", class_="company")[0].text
            job_title = j.find("span", class_="title").text
            job_description = j.find_all("span", class_="company")[1].text + "/" + j.find("span", class_="region company").text
            job_link = j.find_all("a")[-1]["href"]
            result.append({
                "company_name": company_name,
                "job_title": job_title,
                "job_description": job_description,
                "job_link": f"https://weworkremotely.com/{job_link}"
            })

    return result

# Flask 라우팅
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    # 검색 코드
    berlin_jobs = scrape_berlin(keyword)
    web3_jobs = scrape_web3(keyword)
    wework_jobs = scrape_wework(keyword)

    return render_template("search.html", keyword=keyword, berlin_jobs=berlin_jobs, web3_jobs=web3_jobs, wework_jobs=wework_jobs)

# 메인 함수
if __name__ == "__main__":
    app.run("0.0.0.0")