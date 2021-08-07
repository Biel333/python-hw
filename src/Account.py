class Account:

    def __init__(self, owner_id, balance):

        self.owner = "{}".format(owner_id)
        if not isinstance(balance, int) and not isinstance(balance, float) or balance < 0:
            balance = 0.0
        self.__balance = balance
        print("Account({}) was created!".format(id(self)))

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if not isinstance(amount, int) and not isinstance(amount, float) or amount < 0:
            amount = 0.0
        self.__balance += amount

    def withdraw(self, amount):
        if amount < 0 or not isinstance(amount, int) or not isinstance(amount, float):
            amount = 0.0
        self.__balance -= amount
        return amount

    def transfer(self, other_account, amount):
        self.withdraw(amount)
        other_account.deposit(amount)

    def close(self):
        if self.__balance > 0:
            print("Can't close not empty account!")
        else:
            print("Account: {} was closed!".format(self))
            del self

    def __repr__(self):
        return "{}:{}".format(self.owner, self.__balance)
