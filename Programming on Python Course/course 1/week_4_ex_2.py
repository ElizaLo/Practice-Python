class Value:

    def __init__(self):
        self.amount = None

    @staticmethod
    def _prepare_value(value, commission):
        if 1 < commission or commission < 0:
            raise ValueError('Комиссия должна быть числом от 0.0 до 1.0\n commission: {}'.format(commission))
        return int(value - (value * commission))

    def __get__(self, instance, owner):
        return self.amount

    def __set__(self, instance, value):
        self.amount = self._prepare_value(value, instance.commission)


class Account:

    amount = Value()

    def __init__(self, commission):
        self.commission = commission


new_account = Account(0.1)
new_account.amount = 100
print(new_account.amount)
