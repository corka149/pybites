from collections import deque


def rotate(string: str, n: int):
    """Rotate characters in a string.
       Expects string and n (int) for number of characters to move.
    """
    string = deque(string)
    string.rotate(n * -1)
    return ''.join(string)


''' Pybite solution
def rotate(string, n):
    """Rotate characters in a string.
       Expects string and n (int) for number of characters to move.
    """
    return string[n:] + string[:n]
'''


if __name__ == '__main__':
    assert rotate('hello', 2) == 'llohe'
    assert rotate('hello', -2) == 'lohel'
