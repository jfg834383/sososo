import requests
from bs4 import BeautifulSoup
URL = f"https://www.inflearn.com/courses/it-programming?order=seq&skill=javascript"

def get_last_page():
    request = requests.get(URL)

    print(request)

    soup = BeautifulSoup(request.text, 'html.parser')

    result = soup.find("div", {"class":"pagination_container"})

    page = []
    result = result.find_all("a")

    for result in result[1:]:
        page.append(int(result.string))

    return page[-1]

def extract_course(page):
    course = []
    for page in range(page):
        page + 1
        page = requests.get(f"{URL}&page={page}")

        soup = BeautifulSoup(page.text, 'html.parser')
        results = soup.find_all("div", {"class": "course_card_item"})
        for result in results:
            content = extract_course_content(result)
            course.append(content)
    return course


def extract_course_content(html):
    desription = html.find("p", {"class":"course_description"}).string
    level = html.find("div", {"class": "course_level"}).text
    skills = html.find("div", {"class": "course_skills"}).text
    return{
        "description": desription,
        "level": level,
        "skills": skills
        }


def get_course():
    page = get_last_page()
    course = extract_course(page)
    return course

print(get_course())