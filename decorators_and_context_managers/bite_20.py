class Account:

    def __init__(self):
        self._transactions = []

    @property
    def balance(self):
        return sum(self._transactions)

    def __add__(self, amount):
        self._transactions.append(amount)

    def __sub__(self, amount):
        self._transactions.append(-amount)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        while self.balance < 0:
            self._transactions = self._transactions[:-1]

    """ Pybite Solution
     def __enter__(self):
        self._copy_transactions = list(self._transactions)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.balance < 0:
            print('Balance below 0, rolling back transaction')
            self._transactions = self._copy_transactions   
    """


if __name__ == '__main__':
    acc1 = Account()
    acc1 + 3
    assert acc1.balance == 3
    with acc1 as acc:
        acc1 - 5
        acc1 - 2
        acc1 - 12
        assert acc1.balance == -16
    assert acc1.balance == 3
