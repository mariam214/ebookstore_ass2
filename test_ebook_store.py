# test_ebook_store.py

from ebook_store import *#i started by importing the file ebook_store that i made in it all the clasess


def setup_ebook_store():
    """I will be Seting up the e-book store with it including 10 books."""
    catalog = EBook_Catalog()
    # I have Added 10 sample e-books to the catalog
    ebooks = [
        EBook(1, "Python Programming", "Afshan Parker", "2023-01-01", "Programming", 29.99),
        EBook(2, "Data Science Fundamentals", "Jane Smith", "2023-02-01", "Data Science", 34.99),
        EBook(3, "Introduction to Emirati Culture", "Fatima Al Suwaidi", "2023-03-01", "Culture", 24.99),
        EBook(4, "History of the UAE", "Omar Al Muhairi", "2023-04-01", "History", 39.99),
        EBook(5, "Desert Flora and Fauna", "Khalid Al Jaber", "2023-05-01", "Nature", 19.99),
        EBook(6, "Emirati Poetry Anthology", "Majed Al Qasimi", "2023-06-01", "Poetry", 21.99),
        EBook(7, "The Pearl Diver", "Maryam Al Maazmi", "2023-07-01", "Fiction", 15.99),
        EBook(8, "Traditional Emirati Recipes", "Aisha Al Nuaimi", "2023-08-01", "Cooking", 18.99),
        EBook(9, "Guide to Astronomy", "Salem Al Falasi", "2023-09-01", "Science", 27.99),
        EBook(10, "Digital Marketing Basics", "Laila Al Sharqi", "2023-10-01", "Business", 22.99)
    ]
    for ebook in ebooks:
        catalog.add_e_book(ebook)
    return catalog


def simulate_customer_one(catalog):
    """After that i will Simulate actions for Customer 1 which i made her name mariam alzaabi."""
    print("\n📚📜 *** Customer 1 Receipt: Mariam Al Zaabi *** 📜📚")
    customer1 = Customer(1, "Mariam Al Zaabi", "mariam@example.com", isLoyalMember=True)
    cart1 = ShoppingCart()

    # Mariam adds three books to her cart
    cart1.add_item(catalog.get_e_book(1))  # she had adedd Python Programming ebook
    cart1.add_item(catalog.get_e_book(3))  # then adedd the Introduction to Emirati Culture ebook
    cart1.add_item(catalog.get_e_book(5))  # then she adedd the Desert Flora and Fauna ebook

    # Then Mariam decides to remove one book and add another
    print("🛒 Mariam removes 'Python Programming' from her cart.")
    cart1.remove_item(1)
    print("🛒 Mariam adds 'Emirati Poetry Anthology' to her cart.")
    cart1.add_item(catalog.get_e_book(6))  # she had adedd Emirati Poetry Anthology ebook

    # Now i will be creating an order from the cart's total price
    total_price = cart1.calculate_total_price()
    order1 = Order(1, "2023-11-07", totalAmount=total_price)

    # And then i can Apply loyalty discount if the customer has one
    discount = Discount(1, "Loyalty Discount", 5.0)
    if discount.check_loyal_member(customer1):
        order1.apply_discounts(discount)

    # Finaly i will Generate invoice and display the details
    invoice1 = order1.generate_invoice()
    print("===================================")
    print("🧾 INVOICE FOR MARIAM AL ZAABI 🧾")
    print("===================================")
    print("📅 Date: 2023-11-07")
    print("👤 Customer: Mariam Al Zaabi")
    print("\n--- Items Purchased ---")
    for item in cart1.get_items():
        print(f"📖 {item.get_title()} - AED {item.get_price():.2f}")

    print("\n--- Charges ---")
    print(f"Subtotal: AED {total_price:.2f}")
    print(f"Discount (Loyalty): -AED {discount.get_discountPrice():.2f}")
    print(f"VAT (5%): AED {invoice1.calculate_final_total_price() - (total_price - discount.get_discountPrice()):.2f}")
    print(f"Total: AED {invoice1.calculate_final_total_price():.2f}")
    print("===================================")
    print("Thank you for shopping at the E-Book Store! 📚😊\n")


def simulate_customer_two(catalog):
    """Now i will Simulate actions for Customer 2 which her name is mahra and she will be shopping in our ebook."""
    print("\n📚📜 *** Customer 2 Receipt: Mahra Al Shrouqi *** 📜📚")
    customer2 = Customer(2, "Mahra Al Shrouqi", "mahra@example.com", isLoyalMember=False)
    cart2 = ShoppingCart()

    # Mahra now will be adding four books to her cart the ones she likes during her shopping
    cart2.add_item(catalog.get_e_book(2))  # she adeddData Science Fundamentals ebook
    cart2.add_item(catalog.get_e_book(4))  # and added History of the UAE ebook
    cart2.add_item(catalog.get_e_book(8))  #then adedd Traditional Emirati Recipes ebook
    cart2.add_item(catalog.get_e_book(10))  # and adedd Digital Marketing Basics ebook to her cart

    # Mahra decides to replace one book in her cart
    print("🛒 Mahra removes 'Digital Marketing Basics' from her cart.")
    cart2.remove_item(10)
    print("🛒 Mahra adds 'Guide to Astronomy' to her cart.")
    cart2.add_item(catalog.get_e_book(9))  # Guide to Astronomy

    # Create an order from the cart's total price
    total_price = cart2.calculate_total_price()
    order2 = Order(2, "2023-11-07", totalAmount=total_price)

    # Generate invoice without loyalty discount and display details
    invoice2 = order2.generate_invoice()
    print("===================================")
    print("🧾 INVOICE FOR MAHRA AL SHROUQI 🧾")
    print("===================================")
    print("📅 Date: 2023-11-07")
    print("👤 Customer: Mahra Al Shrouqi")
    print("\n--- Items Purchased ---")
    for item in cart2.get_items():
        print(f"📖 {item.get_title()} - AED {item.get_price():.2f}")

    print("\n--- Charges ---")
    print(f"Subtotal: AED {total_price:.2f}")
    print("No Discount Applied")
    print(f"VAT (5%): AED {invoice2.calculate_final_total_price() - total_price:.2f}")
    print(f"Total: AED {invoice2.calculate_final_total_price():.2f}")
    print("===================================")
    print("Thank you for shopping at the E-Book Store! 📚😊\n")


# Run simulation for the e-book store
if __name__ == "__main__":
    # Set up the e-book store with a catalog of 10 books
    catalog = setup_ebook_store()

    # Simulate actions for two customers
    simulate_customer_one(catalog)
    simulate_customer_two(catalog)

    print("The Simulation has been completed suceffely.")
