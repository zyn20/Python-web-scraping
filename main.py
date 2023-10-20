# from bs4 import BeautifulSoup
# import requests
# html_txt = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=West+India&cboWorkExp1=5').text
# soup = BeautifulSoup(html_txt,'lxml')
# jobs = soup.findAll('li', class_='clearfix job-bx wht-shd-bx')
# for job in jobs:
#     job_post  = job.find('span', class_ = 'sim-posted').text
#     str_obj = job.find('ul', class_= 'top-jd-dtl clearfix').text
#     experience = str_obj.
#
#     print(type(experience_req))
#     print(job_post)
#     print(experience_req)

#skills = jobs.find('span', class_='')

#print(jobs)
#for job in jobs:
    #span_ = job.span.text
    #print(span_)

#for job in jobs:
    #job_title = job.h3.text
    #print(job_title)
from bs4 import BeautifulSoup
import requests
import re

html_txt = requests.get(
    'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=West+India&cboWorkExp1=5').text
soup = BeautifulSoup(html_txt, 'lxml')
jobs = soup.findAll('li', class_='clearfix job-bx wht-shd-bx')

for job in jobs:
    job_posted = job.find('span', class_='sim-posted').text.strip()
    job_details = job.find('ul', class_='top-jd-dtl clearfix').text.strip()
    job_link = job.a['href']
    jobs_title = job.h3.text.strip()


    experience_pattern = r'card_travel(\d+)\s*-\s*(\d+)\s*yrs'
    experience_match = re.search(experience_pattern, job_details)
    if experience_match:
        min_experience = experience_match.group(1)
        max_experience = experience_match.group(2)
        experience_req = f"{min_experience} - {max_experience} years"
    else:
        experience_req = "Experience not specified"

    print('Link:', job_link)
    print("Company Name:", jobs_title)
    print("Posted:", job_posted)
    print("Experience Required:", experience_req)
    print("---")
