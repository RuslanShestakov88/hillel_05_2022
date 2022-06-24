class Price:
    def __init__(self, amount: int, currency: str) -> None:
        self.amount = amount
        self.currency = currency

    def __str__(self) -> str:
        return f"price is {self.amount} {self.currency}"

    def __add__(self, other: "Price") -> "Price":
        results = Price(amount=self.amount + other.amount, currency=self.currency)
        return results

    def __sub__(self, other: "Price") -> "Price":
        results = Price(amount=self.amount - other.amount, currency=self.currency)
        return results


a = Price(13, "usd")
b = Price(300, "usd")
c = a - b
print(a)
print(b)
print(c)
