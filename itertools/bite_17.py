import itertools

from typing import List


def friends_teams(friends: List[str], team_size=2, order_does_matter=True):
    if order_does_matter:
        return list(itertools.permutations(friends, team_size))
    else:
        return list(itertools.combinations(friends, team_size))


if __name__ == '__main__':
    print(friends_teams(['Bob', 'Alice', 'Cesar', 'Daisy']))
