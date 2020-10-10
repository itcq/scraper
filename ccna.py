import requests
from bs4 import BeautifulSoup

URL = "https://www.indeed.com/jobs?q=ccna"
SOUP = BeautifulSoup(requests.get(URL).content, 'html.parser')

def get_num_jobs():
    raw_num_jobs = SOUP.find('div', attrs={'id': 'searchCountPages'})
    num_jobs = raw_num_jobs.contents[0].split()[3]
    return num_jobs

if __name__  == "__main__":
    print (f'ccna - USA: {get_num_jobs()}')

print('------')

URL = "https://www.indeed.com/jobs?q=ccna&l=alabama"
SOUP = BeautifulSoup(requests.get(URL).content, 'html.parser')

def get_num_jobs():
    raw_num_jobs = SOUP.find('div', attrs={'id': 'searchCountPages'})
    num_jobs = raw_num_jobs.contents[0].split()[3]
    return num_jobs

if __name__  == "__main__":
    print (f'Alabama: {get_num_jobs()}')

print ('------')

URL = "https://www.indeed.com/jobs?q=ccna&l=alaska"
SOUP = BeautifulSoup(requests.get(URL).content, 'html.parser')

def get_num_jobs():
    raw_num_jobs = SOUP.find('div', attrs={'id': 'searchCountPages'})
    num_jobs = raw_num_jobs.contents[0].split()[3]
    return num_jobs

if __name__  == "__main__":
    print (f'Alaska: {get_num_jobs()}')

print ('------')

URL = "https://www.indeed.com/jobs?q=ccna&l=arizona"
SOUP = BeautifulSoup(requests.get(URL).content, 'html.parser')

def get_num_jobs():
    raw_num_jobs = SOUP.find('div', attrs={'id': 'searchCountPages'})
    num_jobs = raw_num_jobs.contents[0].split()[3]
    return num_jobs

if __name__  == "__main__":
    print (f'Arizona: {get_num_jobs()}')

print ('------')

URL = "https://www.indeed.com/jobs?q=ccna&l=arkansas"
SOUP = BeautifulSoup(requests.get(URL).content, 'html.parser')

def get_num_jobs():
    raw_num_jobs = SOUP.find('div', attrs={'id': 'searchCountPages'})
    num_jobs = raw_num_jobs.contents[0].split()[3]
    return num_jobs

if __name__  == "__main__":
    print (f'Arkansas: {get_num_jobs()}')

print ('------')

URL = "https://www.indeed.com/jobs?q=ccna&l=california"
SOUP = BeautifulSoup(requests.get(URL).content, 'html.parser')

def get_num_jobs():
    raw_num_jobs = SOUP.find('div', attrs={'id': 'searchCountPages'})
    num_jobs = raw_num_jobs.contents[0].split()[3]
    return num_jobs

if __name__  == "__main__":
    print (f'California: {get_num_jobs()}')

print ('------')

URL = "https://www.indeed.com/jobs?q=ccna&l=colorado"
SOUP = BeautifulSoup(requests.get(URL).content, 'html.parser')

def get_num_jobs():
    raw_num_jobs = SOUP.find('div', attrs={'id': 'searchCountPages'})
    num_jobs = raw_num_jobs.contents[0].split()[3]
    return num_jobs

if __name__  == "__main__":
    print (f'Colorado: {get_num_jobs()}')

print ('------')

URL = "https://www.indeed.com/jobs?q=ccna&l=connecticut"
SOUP = BeautifulSoup(requests.get(URL).content, 'html.parser')

def get_num_jobs():
    raw_num_jobs = SOUP.find('div', attrs={'id': 'searchCountPages'})
    num_jobs = raw_num_jobs.contents[0].split()[3]
    return num_jobs

if __name__  == "__main__":
    print (f'Connecticut: {get_num_jobs()}')

print ('------')

URL = "https://www.indeed.com/jobs?q=ccna&l=Delaware"
SOUP = BeautifulSoup(requests.get(URL).content, 'html.parser')

def get_num_jobs():
    raw_num_jobs = SOUP.find('div', attrs={'id': 'searchCountPages'})
    num_jobs = raw_num_jobs.contents[0].split()[3]
    return num_jobs

if __name__  == "__main__":
    print (f'Delaware: {get_num_jobs()}')

print ('------')

URL = "https://www.indeed.com/jobs?q=ccna&l=florida"
SOUP = BeautifulSoup(requests.get(URL).content, 'html.parser')

def get_num_jobs():
    raw_num_jobs = SOUP.find('div', attrs={'id': 'searchCountPages'})
    num_jobs = raw_num_jobs.contents[0].split()[3]
    return num_jobs

if __name__  == "__main__":
    print (f'Florida: {get_num_jobs()}')

print ('------')

URL = "https://www.indeed.com/jobs?q=ccna&l=Georgia"
SOUP = BeautifulSoup(requests.get(URL).content, 'html.parser')

def get_num_jobs():
    raw_num_jobs = SOUP.find('div', attrs={'id': 'searchCountPages'})
    num_jobs = raw_num_jobs.contents[0].split()[3]
    return num_jobs

if __name__  == "__main__":
    print (f'Georgia: {get_num_jobs()}')

print ('------')

URL = "https://www.indeed.com/jobs?q=ccna&l=hawaii"
SOUP = BeautifulSoup(requests.get(URL).content, 'html.parser')

def get_num_jobs():
    raw_num_jobs = SOUP.find('div', attrs={'id': 'searchCountPages'})
    num_jobs = raw_num_jobs.contents[0].split()[3]
    return num_jobs

if __name__  == "__main__":
    print (f'Hawaii: {get_num_jobs()}')

print ('------')

URL = "https://www.indeed.com/jobs?q=ccna&l=idaho"
SOUP = BeautifulSoup(requests.get(URL).content, 'html.parser')

def get_num_jobs():
    raw_num_jobs = SOUP.find('div', attrs={'id': 'searchCountPages'})
    num_jobs = raw_num_jobs.contents[0].split()[3]
    return num_jobs

if __name__  == "__main__":
    print (f'Idaho: {get_num_jobs()}')

print ('------')

URL = "https://www.indeed.com/jobs?q=ccna&l=illinois"
SOUP = BeautifulSoup(requests.get(URL).content, 'html.parser')

def get_num_jobs():
    raw_num_jobs = SOUP.find('div', attrs={'id': 'searchCountPages'})
    num_jobs = raw_num_jobs.contents[0].split()[3]
    return num_jobs

if __name__  == "__main__":
    print (f'Illinois: {get_num_jobs()}')

print ('------')

URL = "https://www.indeed.com/jobs?q=ccna&l=indiana"
SOUP = BeautifulSoup(requests.get(URL).content, 'html.parser')

def get_num_jobs():
    raw_num_jobs = SOUP.find('div', attrs={'id': 'searchCountPages'})
    num_jobs = raw_num_jobs.contents[0].split()[3]
    return num_jobs

if __name__  == "__main__":
    print (f'Indiana: {get_num_jobs()}')

print ('------')

URL = "https://www.indeed.com/jobs?q=ccna&l=iowa"
SOUP = BeautifulSoup(requests.get(URL).content, 'html.parser')

def get_num_jobs():
    raw_num_jobs = SOUP.find('div', attrs={'id': 'searchCountPages'})
    num_jobs = raw_num_jobs.contents[0].split()[3]
    return num_jobs

if __name__  == "__main__":
    print (f'Iowa: {get_num_jobs()}')

print ('------')

URL = "https://www.indeed.com/jobs?q=ccna&l=kansas"
SOUP = BeautifulSoup(requests.get(URL).content, 'html.parser')

def get_num_jobs():
    raw_num_jobs = SOUP.find('div', attrs={'id': 'searchCountPages'})
    num_jobs = raw_num_jobs.contents[0].split()[3]
    return num_jobs

if __name__  == "__main__":
    print (f'Kansas: {get_num_jobs()}')

print ('------')

URL = "https://www.indeed.com/jobs?q=ccna&l=kentucky"
SOUP = BeautifulSoup(requests.get(URL).content, 'html.parser')

def get_num_jobs():
    raw_num_jobs = SOUP.find('div', attrs={'id': 'searchCountPages'})
    num_jobs = raw_num_jobs.contents[0].split()[3]
    return num_jobs

if __name__  == "__main__":
    print (f'Kentucky: {get_num_jobs()}')

print ('------')

URL = "https://www.indeed.com/jobs?q=ccna&l=Louisiana"
SOUP = BeautifulSoup(requests.get(URL).content, 'html.parser')

def get_num_jobs():
    raw_num_jobs = SOUP.find('div', attrs={'id': 'searchCountPages'})
    num_jobs = raw_num_jobs.contents[0].split()[3]
    return num_jobs

if __name__  == "__main__":
    print (f'Louisiana: {get_num_jobs()}')

print ('------')

URL = "https://www.indeed.com/jobs?q=ccna&l=maine"
SOUP = BeautifulSoup(requests.get(URL).content, 'html.parser')

def get_num_jobs():
    raw_num_jobs = SOUP.find('div', attrs={'id': 'searchCountPages'})
    num_jobs = raw_num_jobs.contents[0].split()[3]
    return num_jobs

if __name__  == "__main__":
    print (f'Maine: {get_num_jobs()}')

print ('------')

URL = "https://www.indeed.com/jobs?q=ccna&l=maryland"
SOUP = BeautifulSoup(requests.get(URL).content, 'html.parser')

def get_num_jobs():
    raw_num_jobs = SOUP.find('div', attrs={'id': 'searchCountPages'})
    num_jobs = raw_num_jobs.contents[0].split()[3]
    return num_jobs

if __name__  == "__main__":
    print (f'Maryland: {get_num_jobs()}')

print ('------')

URL = "https://www.indeed.com/jobs?q=ccna&l=massachusetts"
SOUP = BeautifulSoup(requests.get(URL).content, 'html.parser')

def get_num_jobs():
    raw_num_jobs = SOUP.find('div', attrs={'id': 'searchCountPages'})
    num_jobs = raw_num_jobs.contents[0].split()[3]
    return num_jobs

if __name__  == "__main__":
    print (f'Massachusetts: {get_num_jobs()}')

print ('------')

URL = "https://www.indeed.com/jobs?q=ccna&l=michigan"
SOUP = BeautifulSoup(requests.get(URL).content, 'html.parser')

def get_num_jobs():
    raw_num_jobs = SOUP.find('div', attrs={'id': 'searchCountPages'})
    num_jobs = raw_num_jobs.contents[0].split()[3]
    return num_jobs

if __name__  == "__main__":
    print (f'Michigan: {get_num_jobs()}')

print ('------')

URL = "https://www.indeed.com/jobs?q=ccna&l=minnesota"
SOUP = BeautifulSoup(requests.get(URL).content, 'html.parser')

def get_num_jobs():
    raw_num_jobs = SOUP.find('div', attrs={'id': 'searchCountPages'})
    num_jobs = raw_num_jobs.contents[0].split()[3]
    return num_jobs

if __name__  == "__main__":
    print (f'Minnesota: {get_num_jobs()}')

print ('------')

URL = "https://www.indeed.com/jobs?q=ccna&l=mississippi"
SOUP = BeautifulSoup(requests.get(URL).content, 'html.parser')

def get_num_jobs():
    raw_num_jobs = SOUP.find('div', attrs={'id': 'searchCountPages'})
    num_jobs = raw_num_jobs.contents[0].split()[3]
    return num_jobs

if __name__  == "__main__":
    print (f'Mississippi: {get_num_jobs()}')

print ('------')

URL = "https://www.indeed.com/jobs?q=ccna&l=missouri"
SOUP = BeautifulSoup(requests.get(URL).content, 'html.parser')

def get_num_jobs():
    raw_num_jobs = SOUP.find('div', attrs={'id': 'searchCountPages'})
    num_jobs = raw_num_jobs.contents[0].split()[3]
    return num_jobs

if __name__  == "__main__":
    print (f'Missouri: {get_num_jobs()}')

print ('------')

URL = "https://www.indeed.com/jobs?q=ccna&l=montana"
SOUP = BeautifulSoup(requests.get(URL).content, 'html.parser')

def get_num_jobs():
    raw_num_jobs = SOUP.find('div', attrs={'id': 'searchCountPages'})
    num_jobs = raw_num_jobs.contents[0].split()[3]
    return num_jobs

if __name__  == "__main__":
    print (f'Montana: {get_num_jobs()}')

print ('------')

URL = "https://www.indeed.com/jobs?q=ccna&l=nebraska"
SOUP = BeautifulSoup(requests.get(URL).content, 'html.parser')

def get_num_jobs():
    raw_num_jobs = SOUP.find('div', attrs={'id': 'searchCountPages'})
    num_jobs = raw_num_jobs.contents[0].split()[3]
    return num_jobs

if __name__  == "__main__":
    print (f'Nebraska: {get_num_jobs()}')

print ('------')

URL = "https://www.indeed.com/jobs?q=ccna&l=nevada"
SOUP = BeautifulSoup(requests.get(URL).content, 'html.parser')

def get_num_jobs():
    raw_num_jobs = SOUP.find('div', attrs={'id': 'searchCountPages'})
    num_jobs = raw_num_jobs.contents[0].split()[3]
    return num_jobs

if __name__  == "__main__":
    print (f'Nevada: {get_num_jobs()}')

print ('------')

URL = "https://www.indeed.com/jobs?q=ccna&l=New+Hampshire"
SOUP = BeautifulSoup(requests.get(URL).content, 'html.parser')

def get_num_jobs():
    raw_num_jobs = SOUP.find('div', attrs={'id': 'searchCountPages'})
    num_jobs = raw_num_jobs.contents[0].split()[3]
    return num_jobs

if __name__  == "__main__":
    print (f'New Hampshire: {get_num_jobs()}')

print ('------')

URL = "https://www.indeed.com/jobs?q=ccna&l=new+jersey"
SOUP = BeautifulSoup(requests.get(URL).content, 'html.parser')

def get_num_jobs():
    raw_num_jobs = SOUP.find('div', attrs={'id': 'searchCountPages'})
    num_jobs = raw_num_jobs.contents[0].split()[3]
    return num_jobs

if __name__  == "__main__":
    print (f'New Jersey: {get_num_jobs()}')

print ('------')

URL = "https://www.indeed.com/jobs?q=ccna&l=new+mexico"
SOUP = BeautifulSoup(requests.get(URL).content, 'html.parser')

def get_num_jobs():
    raw_num_jobs = SOUP.find('div', attrs={'id': 'searchCountPages'})
    num_jobs = raw_num_jobs.contents[0].split()[3]
    return num_jobs

if __name__  == "__main__":
    print (f'New Mexico: {get_num_jobs()}')

print ('------')

URL = "https://www.indeed.com/jobs?q=ccna&l=new+york"
SOUP = BeautifulSoup(requests.get(URL).content, 'html.parser')

def get_num_jobs():
    raw_num_jobs = SOUP.find('div', attrs={'id': 'searchCountPages'})
    num_jobs = raw_num_jobs.contents[0].split()[3]
    return num_jobs

if __name__  == "__main__":
    print (f'New York: {get_num_jobs()}')

print ('------')

URL = "https://www.indeed.com/jobs?q=ccna&l=north+carolina"
SOUP = BeautifulSoup(requests.get(URL).content, 'html.parser')

def get_num_jobs():
    raw_num_jobs = SOUP.find('div', attrs={'id': 'searchCountPages'})
    num_jobs = raw_num_jobs.contents[0].split()[3]
    return num_jobs

if __name__  == "__main__":
    print (f'North Carolina: {get_num_jobs()}')

print ('------')

URL = "https://www.indeed.com/jobs?q=ccna&l=north+dakota"
SOUP = BeautifulSoup(requests.get(URL).content, 'html.parser')

def get_num_jobs():
    raw_num_jobs = SOUP.find('div', attrs={'id': 'searchCountPages'})
    num_jobs = raw_num_jobs.contents[0].split()[3]
    return num_jobs

if __name__  == "__main__":
    print (f'North Dakota: {get_num_jobs()}')

print ('------')

URL = "https://www.indeed.com/jobs?q=ccna&l=ohio"
SOUP = BeautifulSoup(requests.get(URL).content, 'html.parser')

def get_num_jobs():
    raw_num_jobs = SOUP.find('div', attrs={'id': 'searchCountPages'})
    num_jobs = raw_num_jobs.contents[0].split()[3]
    return num_jobs

if __name__  == "__main__":
    print (f'Ohio: {get_num_jobs()}')

print ('------')

URL = "https://www.indeed.com/jobs?q=ccna&l=oklahoma"
SOUP = BeautifulSoup(requests.get(URL).content, 'html.parser')

def get_num_jobs():
    raw_num_jobs = SOUP.find('div', attrs={'id': 'searchCountPages'})
    num_jobs = raw_num_jobs.contents[0].split()[3]
    return num_jobs

if __name__  == "__main__":
    print (f'Oklahoma: {get_num_jobs()}')

print ('------')

URL = "https://www.indeed.com/jobs?q=ccna&l=oregon"
SOUP = BeautifulSoup(requests.get(URL).content, 'html.parser')

def get_num_jobs():
    raw_num_jobs = SOUP.find('div', attrs={'id': 'searchCountPages'})
    num_jobs = raw_num_jobs.contents[0].split()[3]
    return num_jobs

if __name__  == "__main__":
    print (f'Oregon: {get_num_jobs()}')

print ('------')

URL = "https://www.indeed.com/jobs?q=ccna&l=pennsylvania"
SOUP = BeautifulSoup(requests.get(URL).content, 'html.parser')

def get_num_jobs():
    raw_num_jobs = SOUP.find('div', attrs={'id': 'searchCountPages'})
    num_jobs = raw_num_jobs.contents[0].split()[3]
    return num_jobs

if __name__  == "__main__":
    print (f'Pennsylvania: {get_num_jobs()}')

print ('------')

URL = "https://www.indeed.com/jobs?q=ccna&l=rhode+island"
SOUP = BeautifulSoup(requests.get(URL).content, 'html.parser')

def get_num_jobs():
    raw_num_jobs = SOUP.find('div', attrs={'id': 'searchCountPages'})
    num_jobs = raw_num_jobs.contents[0].split()[3]
    return num_jobs

if __name__  == "__main__":
    print (f'Rhode Island: {get_num_jobs()}')

print ('------')

URL = "https://www.indeed.com/jobs?q=ccna&l=south+carolina"
SOUP = BeautifulSoup(requests.get(URL).content, 'html.parser')

def get_num_jobs():
    raw_num_jobs = SOUP.find('div', attrs={'id': 'searchCountPages'})
    num_jobs = raw_num_jobs.contents[0].split()[3]
    return num_jobs

if __name__  == "__main__":
    print (f'South Carolina: {get_num_jobs()}')

print ('------')

URL = "https://www.indeed.com/jobs?q=ccna&l=south+dakota"
SOUP = BeautifulSoup(requests.get(URL).content, 'html.parser')

def get_num_jobs():
    raw_num_jobs = SOUP.find('div', attrs={'id': 'searchCountPages'})
    num_jobs = raw_num_jobs.contents[0].split()[3]
    return num_jobs

if __name__  == "__main__":
    print (f'South Dakota: {get_num_jobs()}')

print ('------')

URL = "https://www.indeed.com/jobs?q=ccna&l=tennessee"
SOUP = BeautifulSoup(requests.get(URL).content, 'html.parser')

def get_num_jobs():
    raw_num_jobs = SOUP.find('div', attrs={'id': 'searchCountPages'})
    num_jobs = raw_num_jobs.contents[0].split()[3]
    return num_jobs

if __name__  == "__main__":
    print (f'Tennessee: {get_num_jobs()}')

print ('------')

URL = "https://www.indeed.com/jobs?q=ccna&l=texas"
SOUP = BeautifulSoup(requests.get(URL).content, 'html.parser')

def get_num_jobs():
    raw_num_jobs = SOUP.find('div', attrs={'id': 'searchCountPages'})
    num_jobs = raw_num_jobs.contents[0].split()[3]
    return num_jobs

if __name__  == "__main__":
    print (f'Texas: {get_num_jobs()}')

print ('------')

URL = "https://www.indeed.com/jobs?q=ccna&l=utah"
SOUP = BeautifulSoup(requests.get(URL).content, 'html.parser')

def get_num_jobs():
    raw_num_jobs = SOUP.find('div', attrs={'id': 'searchCountPages'})
    num_jobs = raw_num_jobs.contents[0].split()[3]
    return num_jobs

if __name__  == "__main__":
    print (f'Utah: {get_num_jobs()}')

print ('------')

URL = "https://www.indeed.com/jobs?q=ccna&l=vermont"
SOUP = BeautifulSoup(requests.get(URL).content, 'html.parser')

def get_num_jobs():
    raw_num_jobs = SOUP.find('div', attrs={'id': 'searchCountPages'})
    num_jobs = raw_num_jobs.contents[0].split()[3]
    return num_jobs

if __name__  == "__main__":
    print (f'Vermont: {get_num_jobs()}')

print ('------')

URL = "https://www.indeed.com/jobs?q=ccna&l=virginia"
SOUP = BeautifulSoup(requests.get(URL).content, 'html.parser')

def get_num_jobs():
    raw_num_jobs = SOUP.find('div', attrs={'id': 'searchCountPages'})
    num_jobs = raw_num_jobs.contents[0].split()[3]
    return num_jobs

if __name__  == "__main__":
    print (f'Virginia: {get_num_jobs()}')

print ('------')

URL = "https://www.indeed.com/jobs?q=ccna&l=washington"
SOUP = BeautifulSoup(requests.get(URL).content, 'html.parser')

def get_num_jobs():
    raw_num_jobs = SOUP.find('div', attrs={'id': 'searchCountPages'})
    num_jobs = raw_num_jobs.contents[0].split()[3]
    return num_jobs

if __name__  == "__main__":
    print (f'Washington: {get_num_jobs()}')

print ('------')

URL = "https://www.indeed.com/jobs?q=ccna&l=west+virginia"
SOUP = BeautifulSoup(requests.get(URL).content, 'html.parser')

def get_num_jobs():
    raw_num_jobs = SOUP.find('div', attrs={'id': 'searchCountPages'})
    num_jobs = raw_num_jobs.contents[0].split()[3]
    return num_jobs

if __name__  == "__main__":
    print (f'West Virginia: {get_num_jobs()}')

print ('------')

URL = "https://www.indeed.com/jobs?q=ccna&l=wisconsin"
SOUP = BeautifulSoup(requests.get(URL).content, 'html.parser')

def get_num_jobs():
    raw_num_jobs = SOUP.find('div', attrs={'id': 'searchCountPages'})
    num_jobs = raw_num_jobs.contents[0].split()[3]
    return num_jobs

if __name__  == "__main__":
    print (f'Wisconsin: {get_num_jobs()}')

print ('------')

URL = "https://www.indeed.com/jobs?q=ccna&l=wyoming"
SOUP = BeautifulSoup(requests.get(URL).content, 'html.parser')

def get_num_jobs():
    raw_num_jobs = SOUP.find('div', attrs={'id': 'searchCountPages'})
    num_jobs = raw_num_jobs.contents[0].split()[3]
    return num_jobs

if __name__  == "__main__":
    print (f'Wyoming: {get_num_jobs()}')

print ('------')