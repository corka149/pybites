import itertools

names = 'Tim Bob Julian Carmen Sofia Mike Kim Andre'.split()
locations = 'DE ES AUS NL BR US'.split()
confirmed = [False, True, True, False, True]


def get_attendees():
    loc_iter = itertools.chain(locations, itertools.repeat('-'))
    conf_iter = itertools.chain(confirmed, itertools.repeat('-'))
    for participant in zip(names, loc_iter, conf_iter):
        print(participant)


""" pybites - solution

from itertools import zip_longest

def get_attendees():
    for participant in zip_longest(names, locations, confirmed, fillvalue='-'):
        print(participant)
"""

if __name__ == '__main__':
    get_attendees()
