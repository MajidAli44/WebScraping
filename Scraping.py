from bs4 import BeautifulSoup

with open("Index.html", 'r') as html_file:
    content=html_file.read()
    # print(content)

    soup=BeautifulSoup(content, 'lxml')
    # print(soup.prettify())


    # tags=soup.find('h5')
    # tags = soup.find_all('h5')
    # print(tags)

    # courses_html_tags=soup.find_all('h5')
    # for courses in courses_html_tags:
        # print(courses)
        # print(courses.text)

    course_card=soup.find_all("div", class_="card")
    for course in course_card:
        # print(course)
        # print(course.h5)
        course_name=course.h5.text
        # course_price=course.a.text
        course_price = course.a.text.split()[-1]

        # print(course_name)
        # print(course_price)

        print(f'{course_name} cost {course_price}')





