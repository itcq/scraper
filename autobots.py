"""This is Indeed Scraper"""

import requests
import random
import csv
from bs4 import BeautifulSoup
from datetime import datetime
from random import randint
from time import sleep

filename = datetime.now().strftime('jobs-%d-%m-%Y-%H-%M.csv')

"""This function gets the number of jobs"""


def get_num_jobs(state, job_type):
    url = f"https://www.indeed.com/jobs?q={job_type}&l=${state}"
    soup = BeautifulSoup(requests.get(url).content, 'html.parser')  # This is an API CALL
    raw_num_jobs = soup.find('div', attrs={'id': 'searchCountPages'})
    num_jobs = raw_num_jobs.contents[0].split()[3]
    sleep(randint(10, 25))
    return num_jobs


def main():
    """This is your main function"""
    states = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut',
              'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana',
              'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts',
              'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada',
              'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota',
              'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota',
              'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin',
              'Wyoming']
    job_type = ['network engineer', 'cybersecurity', 'help+desk', 'ccna', 'comptia', 'azure', 'aws', 'ethical+hacker', 'cloud+engineer']
    random.shuffle(states)
    with open(filename, 'w+', newline='') as csvfile:
        for job in job_type:
            for state in states:
                indeed_results = get_num_jobs(state, job)  # This calls get_num_jobs function
                writer = csv.writer(csvfile)
                writer.writerow([f"{job}: ", f"{state}:", f"{indeed_results}"])
                print(f'{job}: {state}: {indeed_results}')
                print('------')


# def get_state():
#     """How to enter and input This is not being used"""
#     state = input("Enter name of state: ")
#     return state

# This executes your code
if __name__ == "__main__":
    main()  # This calls your main function