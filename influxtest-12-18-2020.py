"""This is Indeed Scraper"""
"""Special shout out to Du'An Lightfoot and Kevin Diaz for the help"""
import requests
import pandas as pd
import pandas
import random
import csv
from bs4 import BeautifulSoup
from random import randint
from time import sleep
from datetime import datetime

from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

# You can generate a Token from the "Tokens Tab" in the UI
token = "-zr6XdCL7_IC335_yH5I5-tvFnryPguPAGqnWGUvc6lVYY5yphNyNS9l-rfN_ffju70KVRgg9oBS7zDmL3kq8Q=="
org = "zachys@gmail.com"
bucket = "buckets"

client = InfluxDBClient(url="https://us-east-1-1.aws.cloud2.influxdata.com", token=token)

"""This function gets the number of jobs"""


def get_num_jobs(state, job_type):
    url = f"https://www.indeed.com/jobs?q={job_type}&l=${state}"
    soup = BeautifulSoup(requests.get(url).content, 'html.parser')  # This is an API CALL
    raw_num_jobs = soup.find('div', attrs={'id': 'searchCountPages'})
    try:
        num_jobs = raw_num_jobs.contents[0].split()[3]
    except AttributeError:
        num_jobs = 0
    sleep(randint(2, 4))
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
    job_type = ['network engineer', 'help desk', 'ccna', 'comptia',
                'azure', 'aws', 'ethical hacker', 'oscp', 'CEH', 'ccie', 'ccnp', 'cloud engineer', 'security analyst',
                'network technician', 'network administrator', 'data scientist']
    random.shuffle(states)

    for job in job_type:
        for state in states:
            indeed_results = get_num_jobs(state, job)  # This calls get_num_jobs function

            write_api = client.write_api(write_options=SYNCHRONOUS)

            point1 = Point("state") \
                    .field(f"{state}", "states") \
 \
            point2 = Point("jobtype") \
                    .field(f"{job}", "jobs") \

            point3 = Point("numberjobs") \
                    .field(f"{indeed_results}", "jobs") \
 \
            write_api.write(bucket, org, point1, point2)


# def get_state():
#     """How to enter and input This is not being used"""
#     state = input("Enter name of state: ")
#     return state
# This executes your code
if __name__ == "__main__":
    main()  # This calls your main function