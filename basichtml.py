from bs4 import BeautifulSoup

with open('home.html','r') as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content,'lxml')
    #find method only grab the first element
    #tags = soup.find('h1')
    #print(tags)
    # find_all method all element
    #tags = soup.find_all('h1')
    #for tag in tags:
        #print(tag.text)
    course_cards = soup.findAll('div',class_='card')
    for course in course_cards:
        course_name = course.h5.text
        price = course.a.text
        course_price = price.split()[-1]
        course_description = course.p.text
        #print(course_description)

        #full = course_price.split()[-1]
        #print(full)

        print(f'{course_name} costs {course_price} and \n Description : {course_description}')





