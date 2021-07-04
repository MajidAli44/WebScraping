from bs4 import BeautifulSoup
import requests
import time

print("Put some skills that you are not familiar with")

# Single Input
unfamiliar_skills=input(">")
print(unfamiliar_skills)


# Multiple Inputs
# unfamiliar_skill=list(map(input(">").split()))
# print(unfamiliar_skill)




html_text=requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=").text
# print(html_text)

soup=BeautifulSoup(html_text,'lxml')
# print(soup.prettify())

def find_jobs():
    jobs = soup.find_all('li', class_="clearfix job-bx wht-shd-bx")

    for job in jobs:
        job_published_date = job.find('span', class_="sim-posted").span.text
        if 'few' not in job_published_date:
            company_name = job.find("h3", class_="joblist-comp-name").text.replace(' ', '')
            skills = job.find('span', class_="srp-skills").text.replace(' ', '')
            job_type = job.find('strong', class_="blkclor").text.replace(' ', '')
            more_info = job.header.h2.a['href']

            if unfamiliar_skills not in skills:
                print(f'Job Type: {job_type}')
                print(f'Company Name: {company_name.strip()}')
                print(f'Required Skills: {skills.strip()}')
                print(f'Published Date: {job_published_date.strip()}')
                print(f'More Info: {more_info}')
                print("-----------------------------------")



if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait=10
        print(f'Waiting {time_wait} minutes...')
        print(time_wait * 60)





