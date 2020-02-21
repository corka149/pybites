from itertools import islice


def running_mean(sequence):
    """Calculate the running mean of the sequence passed in,
       returns a sequence of same length with the averages.
       You can assume all items in sequence are numeric."""
    for i in range(len(sequence)):
        x = i + 1
        yield round(sum(islice(sequence, x)) / x, 2)
