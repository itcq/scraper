import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

filename = datetime.now().strftime('ccna-%d-%m-%Y-%H-%M.csv')

with open(filename, 'w+', newline='') as csvfile:
    def get_num_jobs(state):
        url = f"https://www.indeed.com/jobs?q=ccna&l=${state}"
        soup = BeautifulSoup(requests.get(url).content, 'html.parser')
        raw_num_jobs = soup.find('div', attrs={'id': 'searchCountPages'})
        num_jobs = raw_num_jobs.contents[0].split()[3]
        return num_jobs


    def main():
        states = ["Alabama", "Alaska", "Arizona"]

        for state in states:
            get_num_jobs(state)
            writer = csv.writer(csvfile)
            writer.writerow([f"{state}:", f"{get_num_jobs(state)}"])

    if __name__ == "__main__":
        main()