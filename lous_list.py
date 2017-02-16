# Alex Hicks (awh4kc)
# I figured out how to sort from https://wiki.python.org/moin/HowTo/Sorting

def instructors(department):

    import urllib.request

    stream = "http://stardock.cs.virginia.edu/louslist/Courses/view/" + department
    courses = urllib.request.urlopen(stream)
    professor_names = []

    for course in courses:
        decoded = course.decode("UTF-8").split(";")[4]
        if decoded not in professor_names:
            professor_names.append(decoded)

    return sorted(professor_names)

def class_search(dept_name, has_seats_available = True, level = None, not_before = None, not_after = None):

    import urllib.request

    stream = "http://stardock.cs.virginia.edu/louslist/Courses/view/" + dept_name
    master_course_list = urllib.request.urlopen(stream)
    course_list = []

    for course in master_course_list:
        decoded = course.decode("UTF-8").strip().split(";")
        if has_seats_available is True:
            if int(decoded[15]) >= int(decoded[16]):
                continue

        if level is not None:
            if decoded[1][0] != str(level)[0]:
                continue

        if not_before is not None:
            if int(decoded[12]) < not_before:
                continue

        if not_after is not None:
            if int(decoded[13]) > not_after:
                continue

        course_list.append(decoded)

    return course_list

