from bs4 import BeautifulSoup
import requests

categories = {
    "Java": "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=java&txtLocation=",
    "Python": "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=ft&searchTextText=&txtKeywords=python&txtLocation=",
    "Data Science": "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=data+science&txtLocation=",
    "It Project Manager": "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=as&searchTextText=%22It+Project+Manager%22&txtKeywords=%22It+Project+Manager%22&txtLocation=",
    "Copywriting": "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=copywriting&txtLocation=",
    "Email Marketing": "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=as&searchTextText=%22Email+Marketing%22&txtKeywords=%22Email+Marketing%22&txtLocation=",
    "Web Design, Web Development": "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=as&searchTextText=%22Web+Design+%2C+Web+Development%22&txtKeywords=%22Web+Design+%2C+Web+Development%22&txtLocation="
}

print("\nPlease select a job category:")
for i, category in enumerate(categories.keys(), 1):
    print(f"{i}. {category}")

choice = int(input("\nEnter the number of your chosen category: "))
selected_category = list(categories.keys())[choice - 1]
url = categories[selected_category]

html_text = requests.get(url).text
soup = BeautifulSoup(html_text, "lxml")
jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

print("\n" + "=" * 100)
print(f"{'Job Listings for ' + selected_category.upper():^100}")
print("=" * 100)

for job in jobs:
    company = job.h3.text.strip()
    
    experience_location = job.find('ul', class_='top-jd-dtl clearfix').find_all('li')
    experience = experience_location[0].text.replace('card_travel', '').strip()
    location = experience_location[1].text.replace('location_on', '').strip()

    skills = job.find('span', class_='srp-skills').text.strip().replace(' , ', ',').replace('\n', ' ').strip()

    print("\n" + "-" * 100)
    print(f"Company:      {company}")
    print(f"Experience:   {experience}")
    print(f"Location:     {location}")
    print(f"Skills:       {skills}")
    print("-" * 100)

print("\n" + "=" * 100)
print(f"End of {selected_category} job listings")
print("=" * 100 + "\n")
