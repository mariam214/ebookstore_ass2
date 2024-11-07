#in this file i have adedd all the 8 clasess that i have done already in my UML diagram

#class 1. Ebook
class EBook:
    """Class representing an e-book with specific details."""

    def __init__(self, eBookID, title, author, publicationDate, genre, price):
        # Initializes an e-book with given attributes
        self._eBookID = eBookID
        self._title = title
        self._author = author
        self._publicationDate = publicationDate
        self._genre = genre
        self._price = price

    # Getters
    def get_eBookID(self):
        """Returns the eBook ID."""
        return self._eBookID

    def get_title(self):
        """Returns the title of the e-book."""
        return self._title

    def get_author(self):
        """Returns the author of the e-book."""
        return self._author

    def get_price(self):
        """Retrieves the price of the e-book."""
        return self._price

    # Setters
    def set_price(self, price):
        """Sets the price of the e-book."""
        self._price = price

    def __str__(self):
        """Returns a string representation of the e-book."""
        return f"EBook({self._title}, {self._author}, {self._price})"

#class 2.Ebook_Catalog
class EBook_Catalog:
    """Class representing the catalog of e-books available in the store."""

    def __init__(self):
        # Initializes an empty catalog of e-books
        self._e_books = []  # Protected attribute for storing EBook objects

    def add_e_book(self, e_book):
        """Adds an e-book to the catalog."""
        self._e_books.append(e_book)

    def remove_e_book(self, e_book_id):
        """Removes an e-book from the catalog by its ID."""
        self._e_books = [e_book for e_book in self._e_books if e_book.get_eBookID() != e_book_id]

    def get_e_book(self, e_book_id):
        """Retrieves details of an e-book by ID."""
        for e_book in self._e_books:
            if e_book.get_eBookID() == e_book_id:
                return e_book
        return None

    def __str__(self):
        """Returns a string representation of the e-book catalog."""
        return f"EBook Catalog with {len(self._e_books)} books"

#class 3 is Customer
class Customer:
    """Class representing a customer in the e-book store."""

    def __init__(self, customerID, name, contactInformation, isLoyalMember=False):
        # Initializes a customer with ID, name, contact info, and loyalty status
        self._customerID = customerID
        self._name = name
        self._contactInformation = contactInformation
        self._isLoyalMember = isLoyalMember
        self._cart = ShoppingCart()

    # Getters and Setters
    def get_customerID(self):
        """Returns the customer ID."""
        return self._customerID

    def get_name(self):
        """Returns the customer's name."""
        return self._name

    def get_contactInformation(self):
        """Returns the customer's contact information."""
        return self._contactInformation

    def get_isLoyalMember(self):
        """Returns loyalty membership status."""
        return self._isLoyalMember

    def set_isLoyalMember(self, status):
        """Sets loyalty membership status."""
        self._isLoyalMember = status

    def __str__(self):
        """Returns a string representation of the customer."""
        return f"Customer({self._name}, Loyal: {self._isLoyalMember})"

#class 4.ShoppingCart
class ShoppingCart:
    """Class representing a shopping cart holding items to be purchased."""

    def __init__(self):
        # Initializes a shopping cart with an ID, items list, and quantity
        self._cartID = id(self)
        self._items = []
        self._quantity = 0

    # Getters and Setters
    def get_cartID(self):
        """Returns the cart ID."""
        return self._cartID

    def get_items(self):
        """Returns the items in the cart."""
        return self._items

    def get_quantity(self):
        """Returns the quantity of items in the cart."""
        return self._quantity

    def add_item(self, e_book):
        """Adds an e-book to the cart and increments quantity."""
        self._items.append(e_book)
        self._quantity += 1

    def remove_item(self, e_book_id):
        """Removes an item from the cart by eBookID and decrements quantity."""
        self._items = [item for item in self._items if item.get_eBookID() != e_book_id]
        self._quantity -= 1

    def calculate_total_price(self):
        """Calculates total price for items in the cart."""
        return sum(item.get_price() for item in self._items)

    def __str__(self):
        """Returns a string representation of the shopping cart."""
        return f"ShoppingCart with {self._quantity} items"

#class 5 is Order
class Order:
    """Class representing an order placed by the customer."""

    def __init__(self, orderID, orderDate, totalAmount=0):
        # Initializes an order with ID, date, and total amount
        self._orderID = orderID
        self._orderDate = orderDate
        self._totalAmount = totalAmount

    # Getters and Setters
    def get_orderID(self):
        """Returns the order ID."""
        return self._orderID

    def get_orderDate(self):
        """Returns the order date."""
        return self._orderDate

    def get_totalAmount(self):
        """Returns the total amount of the order."""
        return self._totalAmount

    def set_totalAmount(self, amount):
        """Sets the total amount of the order."""
        self._totalAmount = amount

    def apply_discounts(self, discount):
        """Applies discounts to the order by reducing the total amount."""
        self._totalAmount -= discount.get_discountPrice()

    def generate_invoice(self):
        """Generates an invoice for the order."""
        return Invoice(self._orderID, self, vat=5.0)

    def __str__(self):
        """Returns a string representation of the order."""
        return f"Order({self._orderID}, {self._totalAmount})"

#class 6 is discount
class Discount:
    """Class representing a discount applied to orders."""

    def __init__(self, discountID, promotionSale, discountPrice):
        # Initializes a discount with ID, promotion sale description, and discount price
        self._discountID = discountID
        self._promotionSale = promotionSale
        self._discountPrice = discountPrice

    # Getters
    def get_discountID(self):
        """Returns the discount ID."""
        return self._discountID

    def get_discountPrice(self):
        """Returns the discount price."""
        return self._discountPrice

    def check_loyal_member(self, customer):
        """Checks if the customer is a loyalty program member."""
        return customer.get_isLoyalMember()

    def apply_discounts(self, order):
        """Applies discount to the order if customer is eligible."""
        if self.check_loyal_member(order.customer):
            order.set_totalAmount(order.get_totalAmount() - self._discountPrice)

    def __str__(self):
        """Returns a string representation of the discount."""
        return f"Discount({self._discountID}, {self._promotionSale})"

#class 7 is invoice
class Invoice:
    """Class representing an invoice generated for an order."""

    def __init__(self, invoiceID, order, vat=5.0):
        # Initializes an invoice with ID, associated order, and VAT
        self._invoiceID = invoiceID
        self._order = order
        self._vat = vat
        self._totalPrice = self.calculate_final_total_price()

    # Getters
    def get_invoiceID(self):
        """Returns the invoice ID."""
        return self._invoiceID

    def get_totalPrice(self):
        """Returns the total price including VAT."""
        return self._totalPrice

    def calculate_final_total_price(self):
        """Calculates the final total including VAT."""
        return self._order.get_totalAmount() + (self._order.get_totalAmount() * self._vat / 100)

    def __str__(self):
        """Returns a string representation of the invoice."""
        return f"Invoice({self._invoiceID}, Total: {self._totalPrice})"

#class 8 is Registration
class Registration:
    """Class managing customer registration and validation."""

    def __init__(self, registrationID, name, contactInfo):
        # Initializes registration with ID, name, and contact info
        self._registrationID = registrationID
        self._name = name
        self._contactInfo = contactInfo

    # Getters
    def get_registrationID(self):
        """Returns the registration ID."""
        return self._registrationID

    def validation(self):
        """Validates the registration information."""
        # Implementation of validation process
        pass

    def __str__(self):
        """Returns a string representation of the registration."""
        return f"Registration({self._registrationID}, {self._name})"
