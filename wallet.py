class Wallet:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def add_money(self, amount):
        if amount > 0:
            self.amount += amount
            print(f"Dobaveni sa {amount} {self.currency}")
        else:
            print("Sumata za dobavqne trqbva da e polojitelna")

    def spend_money(self, amount):
        if amount <= self.amount:
            self.amount -= amount
            print(f"Poharcheni sa {amount} {self.currency}")
        else:
            print("Nqma dostatuchno sredstva")

    def show_balance(self):
        print(f"Balans: {self.amount} {self.currency}")


wallet = Wallet(100, "BGN")
wallet.show_balance()
wallet.add_money(50)
wallet.spend_money(30)
wallet.spend_money(150)
wallet.show_balance()