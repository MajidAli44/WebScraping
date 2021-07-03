from bs4 import BeautifulSoup
import requests

html_text=requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=").text
# print(html_text)

soup=BeautifulSoup(html_text,'lxml')
# print(soup.prettify())

jobs=soup.find_all('li', class_="clearfix job-bx wht-shd-bx")

for job in jobs:
    job_published_date = job.find('span', class_="sim-posted").span.text
    if 'few' not in job_published_date:
        company_name = job.find("h3", class_="joblist-comp-name").text.replace(' ', '')
        skills = job.find('span', class_="srp-skills").text.replace(' ', '')
        job_type = job.find('strong', class_="blkclor").text.replace(' ', '')
        more_info=job.header.h2.a['href']

        print(f'Job Type: {job_type}')
        print(f'Company Name: {company_name.strip()}')
        print(f'Required Skills: {skills.strip()}')
        print(f'Published Date: {job_published_date.strip()}')
        print(f'More Info: {more_info}')
        print("-----------------------------------")




