### Python Web Scraping

This Python script is designed to scrape job listings from the TimesJobs website, focusing on Python programming jobs in the West India region. The script utilizes various libraries and techniques for web scraping and data processing.

### 1. **Importing Libraries:**
   - `time`: Allows for introducing delays to prevent overwhelming the server.
   - `BeautifulSoup`: A Python library for parsing HTML content during web scraping.
   - `requests`: Enables sending HTTP requests to a specific URL for data retrieval.
   - `re`: Provides support for using regular expressions in pattern matching.

### 2. **User Input:**
   - Asks the user to input a skill (Python-related skills, in this case) they are unfamiliar with. This input filters job listings.

### 3. **Web Scraping:**
   - Sends a request to the TimesJobs website's search page, targeting Python-related jobs in West India.
   - Parses HTML content of the page using BeautifulSoup.
   - Extracts job listings based on specific HTML tags and classes, including job title, company name, skills required, experience, and posting details.

### 4. **Data Filtering and Saving:**
   - Iterates through job listings.
   - Checks if the unfamiliar skill provided by the user is not among the required skills for the job.
   - If the unfamiliar skill isn't required, job details are saved in text files within the 'posts' directory. Files include company name, job link, posting date, required experience, and skills.

### 5. **Regular Expression Usage:**
   - Regular expressions are used to extract minimum and maximum years of experience required for each job listing.

### 6. **Loop and Waiting:**
   - The script runs in an infinite loop.
   - After scraping and processing job listings, it waits for 10 minutes before running again to avoid server overload.

### 7. **File Output:**
   - Job details are saved in separate text files within the 'posts' directory, uniquely identified by an index number.

### Important Note:
   - The script relies on the specific structure of the TimesJobs website. Changes in the website's structure may require updates to the script for accurate scraping.

### Output Example:
![Sample Output](https://github.com/zyn20/Python-web-scraping/assets/79300060/49c96ce6-f0fe-4087-a6e1-c124c725fa01)
