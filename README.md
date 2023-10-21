# Python-web-scraping
This Python script is designed to scrape job listings from a specific website (TimesJobs) based on user-defined search criteria
specifically focusing on jobs related to Python programming in the West India region.
1. Importing Libraries:
time: Allows the script to introduce delays (in this case, waiting for a specified amount of time).
BeautifulSoup: A popular Python library for web scraping purposes, used here for parsing HTML content.
requests: Enables sending HTTP requests to the specified URL.
re: Provides support for regular expressions.
2. User Input:
Ask the user to input a skill (in this case, Python-related skills) they are unfamiliar with. This skill is then used to filter job listings.
3. Web Scraping:
The script sends a request to the TimesJobs website's search page, specifically targeting Python-related jobs in West India.
It then parses the HTML content of the page using BeautifulSoup.
Job listings are extracted based on specific HTML tags and classes, containing information like job title, company name, skills required, experience, and job posting details.
4. Data Filtering and Saving:
The script iterates through the extracted job listings.
For each job, it checks if the unfamiliar skill input by the user is not present in the required skills for the job.
If the unfamiliar skill is not a requirement for the job, the job details are saved in a text file inside the 'posts' directory. Each file contains details like company name, job link, posting date, required experience, and skills.
5. Regular Expression Usage:
Regular expressions are used to extract the minimum and maximum years of experience required for each job listing.
6. Loop and Waiting:
The script is set to run in an infinite loop.
After scraping and processing the job listings, it waits for 10 minutes before running again. This delay is introduced to prevent overwhelming the server with continuous requests.
7. File Output:
Job details are saved in separate text files within the 'posts' directory, each file uniquely identified by an index number.
Important Note:
This script assumes a specific structure of the TimesJobs website. If the structure of the website changes, the script may need to be updated to match the new structure for accurate scraping.
Output
![image](https://github.com/zyn20/Python-web-scraping/assets/79300060/49c96ce6-f0fe-4087-a6e1-c124c725fa01)

