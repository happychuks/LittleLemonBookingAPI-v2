import datetime
from django.test import TestCase
from .models import Booking, Menu

class BookingTestCase(TestCase):
    def setUp(self):
        Booking.objects.create(first_name="John", reservation_date=datetime.date(2024, 3, 20), reservation_slot=10)

    def test_booking_str_method(self):
        booking = Booking.objects.get(first_name="John")
        self.assertEqual(str(booking), "John")

    def test_booking_reservation_date(self):
        booking = Booking.objects.get(first_name="John")
        self.assertEqual(booking.reservation_date, datetime.date(2024, 3, 20))

    def test_booking_reservation_slot_default_value(self):
        booking = Booking.objects.get(first_name="John")
        self.assertEqual(booking.reservation_slot, 10)

class MenuTestCase(TestCase):
    def setUp(self):
        Menu.objects.create(name="Pizza", price=10, menu_item_description="Delicious pizza with toppings")

    def test_menu_str_method(self):
        menu_item = Menu.objects.get(name="Pizza")
        self.assertEqual(str(menu_item), "Pizza")

    def test_menu_price_not_null(self):
        menu_item = Menu.objects.get(name="Pizza")
        self.assertIsNotNone(menu_item.price)

    def test_menu_description_length(self):
        menu_item = Menu.objects.get(name="Pizza")
        self.assertLessEqual(len(menu_item.menu_item_description), 1000)

    def test_menu_price_greater_than_zero(self):
        menu_item = Menu.objects.get(name="Pizza")
        self.assertGreater(menu_item.price, 0)
