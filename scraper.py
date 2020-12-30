#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Title: Indeed Scraper
Authors: Zach Hill, Kevin Diaz, Du'an Lightfoot
Description:
    Scrapes number of jobs on indeed and uploads this data to an influx db instance
    for graphing and analysis
TODO:
    - Add logging
    - Replace individual influx writes with batch writes to reduce API calls
"""
import json
import sys
from random import randint
from time import sleep

import influxdb_client
import requests
from bs4 import BeautifulSoup
from influxdb_client.client.write_api import SYNCHRONOUS, Point, WriteApi

try:
    with open('config.json', 'r') as conf_file:
        INFLUX_CONFIG = json.load(conf_file)
except FileNotFoundError:
    print("ERROR: Config file does not exist\n"
      "Please create config.json in the root of the project folder\n"
      "Feel free to copy config.json.sample (provided with project)"
    )
    sys.exit(-1)
except json.decoder.JSONDecodeError:
    print("ERROR: Failed to parse config. Check that the JSON is valid\n"
          "Feel free to copy config.json.sample (provided with project)"
    )
    sys.exit(-1)


def get_num_jobs(state: str,
                 search_term: str) -> int:
    """
    Scrape indeed for number of jobs based on given search term

    Args:
        state (str): State in which to search
        search_term (str): Keyword to search for
    Returns:
        num_jobs (int): Number of jobs found on indeed. Zero may be returned on error
    """
    url = f"https://www.indeed.com/jobs?q={search_term.strip()}&l=${state.strip()}"
    soup = BeautifulSoup(requests.get(url).content, 'html.parser')
    raw_num_jobs = soup.find('div', attrs={'id': 'searchCountPages'})
    try:
        num_jobs = int(raw_num_jobs.contents[0].split()[3])
    except (AttributeError, ValueError):
        num_jobs = 0
    return num_jobs

def scrape(states: list,
           search_terms: list,
           write_api: WriteApi,
           measurement: str) -> None:
    """
    Call scraper for each state and search term and write data to influx db

    Args:
        states (list[str]):
        search_terms (list[str]):
        write_api (WriteApi):
        measurement (str):
    """
    for search_term in search_terms:
        for state in states:
            indeed_num_jobs = get_num_jobs(state, search_term)

            # Create influx Point using data
            point = Point(measurement)\
                    .tag("state", state)\
                    .field(search_term, indeed_num_jobs)

            # Upload data to influx db
            write_api.write(
                bucket=INFLUX_CONFIG["bucket"],
                org=INFLUX_CONFIG["org"],
                record=point
            )

            # Delay program to evade indeed DDOS protection
            sleep(randint(2, 4))

def main():
    """Reads resource files, instantiates influxdb api client and executes scraper"""
    with open('resources/states.txt', 'r') as states_file:
        states = states_file.read().splitlines()

    with open('resources/job_titles.txt', 'r') as jobs_file:
        job_titles = jobs_file.read().splitlines()

    with open('resources/certs.txt', 'r') as certs_file:
        certifications = certs_file.read().splitlines()

    # Create influx db API client
    influx_client = influxdb_client.InfluxDBClient(
        url=INFLUX_CONFIG["url"],
        token=INFLUX_CONFIG["token"],
        org=INFLUX_CONFIG["org"]
    )
    influx_write_api = influx_client.write_api(write_options=SYNCHRONOUS)

    scrape(states, job_titles, influx_write_api, "openings_by_title")
    scrape(states, certifications, influx_write_api, "openings_by_cert")

if __name__ == "__main__":
    main()
