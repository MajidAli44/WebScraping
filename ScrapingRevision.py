from bs4 import BeautifulSoup

with open("Index.html",'r') as html_file:
    content=html_file.read()
    # print(content)

    soup=BeautifulSoup(content, 'lxml')
    # print(soup.prettify())
    # tags=soup.find_all('h5')
    # print(tags)

    # courses_html_tags=soup.find_all('h5')
    # for course in courses_html_tags:
    #     print(course.text)

    course_cards=soup.find_all('div', class_='card')
    for course in course_cards:
        course_name=course.h5.text
        course_price=course.a.text.split()[-1]
        print(f'{course_name} and price is {course_price}')

