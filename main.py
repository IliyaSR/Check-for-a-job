import requests
from bs4 import BeautifulSoup
import re


def dev_search_junior():
    url = "https://dev.bg/company/jobs/python/?_job_location=remote%2Cplovdiv&_seniority=intern"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        date_of_post = soup.find_all('span', class_='date date-with-icon')
        name_of_position = soup.find_all('h6', class_='job-title ab-title-placeholder ab-cb-title-placeholder')
        name_of_company = soup.find_all('span', class_='company-name hide-for-small')
        for i in range(len(name_of_position)):
            print(f'Date of Post: {(date_of_post[i].text).strip()}')
            print(f"Job Title: {name_of_position[i].text}")
            print(f'Company Title: {name_of_company[i].text}')
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")


def jobs_search_junior():
    url = 'https://www.jobs.bg/front_job_search.php?subm=1&categories%5B%5D=56&techs%5B%5D=Python&location_sid=2&is_home_based=1&it_level%5B%5D=1'
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        name_of_position = soup.find_all('div', class_='card-title <!--desktop-->')
        name_of_company = soup.find_all('div', class_='secondary-text')
        day_of_post = soup.find_all('div', class_='card-date')

        day_of_posts = [day_of_post[i].text for i in range(len(day_of_post))]

        spans = [name_of_position[i].text for i in range(len(name_of_position))]
        for span in spans:
            cleaned_text = re.sub(r'\bstar\b', '', span.strip())

            match = re.search(r'\b([A-Za-z ]+)\b', cleaned_text)
            job_title = match.group(1)

            current_day_of_post = day_of_posts.pop(0)
            current_post = re.search(r'\b(\d{1,2}\.\d{1,2}\.\d{1,2})\b', current_day_of_post)
            print("Date of Post:", current_post.group(1))
            print("Job Title:", job_title)
            print('Company Title:', name_of_company.pop(0).text)
            print('')
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")



