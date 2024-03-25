class Author:
    def __init__(self, name):
        self.name = name
        self.contracts_list = []
    
    def contracts(self):
        return self.contracts_list
    
    def books(self):
        related_books = []
        for contract in self.contracts_list:
            related_books.append(contract.book)
        return related_books
    
    def sign_contract(self, book, date, royalties):
        new_contract = Contract(book, self, date, royalties)
        self.contracts_list.append(new_contract)
        return new_contract
    
    def total_royalties(self):
        total = 0
        for contract in self.contracts_list:
            total += contract.royalties
        return total



class Book:
    pass


class Contract:
    contract_list = []

    def __init__(self, book, author, date, royalties):
        self.book = book
        self.author = author
        self.date = date
        self.royalties = royalties
        Contract.contract_list.append(self)
    
    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.contract_list if contract.date == date]
