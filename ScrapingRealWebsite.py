from bs4 import BeautifulSoup
import requests
import time

# html_text=requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=").text

# print(html_text)

# soup=BeautifulSoup(html_text,"lxml")

# jobs=soup.find('li', class_ ="clearfix job-bx wht-shd-bx")
# print(jobs)

# jobs=soup.find_all('li', class_ ="clearfix job-bx wht-shd-bx")
# print(jobs)


# For Single


# job=soup.find('li', class_ ="clearfix job-bx wht-shd-bx")
# company_name=job.find("h3", class_= "joblist-comp-name")
# skills=job.find("span", class_="srp-skills")
# category=job.find("strong", class_="blkclor").text.replace(' ','')
# published_date=job.find("span",class_="sim-posted").text
# print(published_date)

# print(f'''
# Job Type: {category}
# Company Name: {company_name.text.replace(' ','')}
# Required Skills: {skills.text.replace(' ','')}
# ''')

# print(company_name.text.replace(' ',''))
# print(skills.text.replace(' ',''))



# For Multiple

# jobs=soup.find_all('li', class_ ="clearfix job-bx wht-shd-bx")
# for job in jobs:
#     company_name = job.find("h3", class_="joblist-comp-name")
#     skills = job.find("span", class_="srp-skills")
#     category = job.find("strong", class_="blkclor").text.replace(' ', '')
#     published_date = job.find("span", class_="sim-posted").text
#
#     print(f'''
#     Job Type: {category}
#     Company Name: {company_name.text.replace(' ', '')}
#     Required Skills: {skills.text.replace(' ', '')}
#     Publihed Date: {published_date}
#     ''')
#
#     print("--------------------------------------------------------------------")




# jobs=soup.find_all('li', class_ ="clearfix job-bx wht-shd-bx")
# for job in jobs:
#     published_date = job.find("span", class_="sim-posted").text
#     if 'few' in published_date:
#         company_name = job.find("h3", class_="joblist-comp-name")
#         skills = job.find("span", class_="srp-skills")
#         category = job.find("strong", class_="blkclor").text.replace(' ', '')
#
#
#         print(f'''
#             Job Type: {category}
#             Company Name: {company_name.text.replace(' ', '')}
#             Required Skills: {skills.text.replace(' ', '')}
#             Published Date: {published_date}
#             ''')
#
#         print("--------------------------------------------------------------------")


# Adding features to the Projects
print("Put some skills that you are not familiar with!")
unfamiliar_skill=input("> ")
print(f"Filtering Out: {unfamiliar_skill}")

def find_jobs():
    html_text = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=").text

    soup = BeautifulSoup(html_text, "lxml")
    jobs = soup.find_all('li', class_="clearfix job-bx wht-shd-bx")
    for index, job in enumerate(jobs):
        published_date = job.find("span", class_="sim-posted").text
        if 'few' in published_date:
            company_name = job.find("h3", class_="joblist-comp-name").text.replace(' ', '')
            skills = job.find("span", class_="srp-skills").text.replace(' ', '')
            more_info = job.header.h2.a["href"]

            if unfamiliar_skill not in skills:
                with open(f'posts/{index}.txt', 'w') as f:
                    f.write(f"Company Name: {company_name.strip()}\n")
                    f.write(f"Required Skills: {skills.strip()}\n")
                    f.write(f"More Info: {more_info}")
                print(f"File Save {index} Successfully")




if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait=10
        print(f'Waiting {time_wait} minutes')
        time.sleep(10 * 60)



