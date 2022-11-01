# https://www.codewars.com/kata/52449b062fb80683ec000024/

def generate_hashtag(s):
    if len(s) > 140 or len(s) == 0:
        return False
    else:
        return '#' + ''.join([i.capitalize() for i in s.split()])