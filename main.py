import time
from bs4 import BeautifulSoup
import requests
import re

print('Enter the Unfamiliar Skills')
unfamiliar_temp = input('>')
unfamiliar_skills = unfamiliar_temp.lower()
print(f'Filtering the Unfamiliar Skill: {unfamiliar_skills} to Provide the Best Results.......')

def findjobs():
    html_txt = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=West+India&cboWorkExp1=5').text
    soup = BeautifulSoup(html_txt, 'lxml')
    jobs = soup.findAll('li', class_='clearfix job-bx wht-shd-bx')

    for index, job in enumerate(jobs):
        job_posted = job.find('span', class_='sim-posted').text.strip()
        job_details = job.find('ul', class_='top-jd-dtl clearfix').text.strip()
        job_link = job.h2.a['href']
        jobs_title = job.h3.text.strip()
        jobs_skills_temp = job.find('span', class_='srp-skills').text.strip()
        jobs_skills = jobs_skills_temp.lower()

        experience_pattern = r'card_travel(\d+)\s*-\s*(\d+)\s*yrs'
        experience_match = re.search(experience_pattern, job_details)
        if experience_match:
            min_experience = experience_match.group(1)
            max_experience = experience_match.group(2)
            experience_req = f"{min_experience} - {max_experience} years"
        else:
            experience_req = "Experience not specified"
        if unfamiliar_skills not in jobs_skills:
            with open(f'posts/{index}_jobs.txt', 'w') as file:
                file.write(f'Company Name: {jobs_title} \n')
                file.write(f'Job Link : {job_link} \n')
                file.write(f'Job Posted : {job_posted}\n')
                file.write(f'Experience Required: {experience_req}\n')
                file.write(f'Skills: {jobs_skills}\n')
            print(f'File Saved: {index}_jobs\n')

if __name__ == '__main__':

        findjobs()
        wait_time = 10
        print(f'Waiting {wait_time} Minutes.... ')
        time.sleep(wait_time * 60)
