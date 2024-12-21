import re
def match_string(string):

        pattern = re.compile('\Bz\B')
        test_case = pattern.search(string)
        return test_case.group()


print(match_string('the revathi is lazy programmer'))
