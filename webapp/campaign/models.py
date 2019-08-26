PROSPECT = 'prospect'
CLOSED = 'closed'
FAILED = 'failed'

class Customer(object):

    def __init__(self, id, name, email):
        self.id =id
        self.name = name
        self.email = email

    @classmethod
    def all(cls):
        return list(CUSTOMERS.values())

    @classmethod
    def one(cls, _id):
        return CUSTOMERS[_id]

    @classmethod
    def update(cls, object):
        CUSTOMERS[object.id] = object


class Campaign(object):

    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.prospect_customers = {}

    def add_prospect(self, customer):
        self.prospect_customers[customer.id] = PROSPECT

    def close_sale(self, customer):
        self.prospect_customers[customer.id] = CLOSED

    def drop_sale(self, customer):
        self.prospect_customers[customer.id] = FAILED

    @classmethod
    def all(cls):
        return list(CAMPAIGNS.values())

    @classmethod
    def one(cls, _id):
        return CAMPAIGNS[_id]

    @classmethod
    def update(cls, object):
        CAMPAIGNS[object.id] = object

CUSTOMERS = {
    i: Customer(i, f'name: {i}', f'{i}@test.com') for i in range(10)}



CAMPAIGNS = {
    i: Campaign(i, f'name: {i}') for i in range(5)
}



'''

def factory(i, obj):
    obj.id = i
    return obj




class Base():

    CLASS_ = {}

    @classmethod
    def all(cls):
        return list(cls.CLASS_.values())

    @classmethod
    def one(cls, _id):
        return cls.CLASS_[_id]

    @classmethod
    def update(cls, object):
        cls.CLASS_[object.id] = object



class Customer(Base):


    def __init__(self, name, email):
        self.id = None
        self.name = name
        self.email = email
        self.__class__.CLASS_ = CUSTOMERS


class Campaign(Base):

    def __init__(self, name):
        self.id = None
        self.name = name
        self.prospect_customers = {}
        self.__class__.CLASS_ = CAMPAIGNS

    def add_prospect(self, customer):
        self.prospect_customers[customer.id] = PROSPECT

    def close_sale(self, customer):
        self.prospect_customers[customer.id] = CLOSED

    def drop_sale(self, customer):
        self.prospect_customers[customer.id] = FAILED


CUSTOMERS = {
    i: factory(i, Customer(f'name: {i}', f'{i}@test.com')) for i in range(10)}



CAMPAIGNS = {
    i: factory(i, Campaign(f'name: {i}'))  for i in range(5)
}

'''


