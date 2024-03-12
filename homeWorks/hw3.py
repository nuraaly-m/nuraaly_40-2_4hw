class Bank:
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def __str__(self):
        return (f'name: {self._name}\n'
              f'balance: {self._balance}')

    def moneyX(self):
        self._balance += int(input('сколько хотите добавить?: '))

    def _kill(self):
        self._balance -= self._balance

    def kill(self):
        self._kill()

    def __jackpot(self):
        self._balance *= 10

    def jackpot(self):
        self.__jackpot()

    # def _sumbalances(self, user):
    #     self._balance += user._balance
    #
    # def sumbalances(self):
    #     self._sumbalances()


user1 = Bank('Nuraaly', 100)
user2 = Bank('Umar', 200)

user1.kill()
user1.moneyX()
user1.jackpot()

print(user1)