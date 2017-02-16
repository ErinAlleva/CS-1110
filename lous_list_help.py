# Alex Hicks (awh4kc)

import urllib.request

department = "CS"

stream = "http://stardock.cs.virginia.edu/louslist/Courses/view/" + department
courses = urllib.request.urlopen(stream)
professors = []
for course in courses:
    if course.decode("UTF-8").split(";")[4] not in professors:
        professors.append(course.decode("UTF-8").split(";")[4])
print(professors)
