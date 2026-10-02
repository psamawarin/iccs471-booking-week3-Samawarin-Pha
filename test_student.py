"""Add your two tests here. Keep the supplied baseline and smoke tests intact."""
import unittest
from models import Booking
from service import move_booking
from copy import deepcopy

# Add a unittest.TestCase class with your two test methods.
# See IA 3.2 for the cases and the expectation you must record before using AI.


class StudentTest(unittest.TestCase):

# Given: an active booking
# When: the booking is moved to the same room and time slot
# Expect: the move succeeds and the booking remains the same
    def test_unchanged_move(self):
        bookings = [Booking(17, "Room 201", 600, 660)]
        before = deepcopy(bookings)
        result = move_booking(bookings, 17, "Room 201", 600, 660)
        self.assertIs(result, bookings[0])
        self.assertEqual(bookings, before)

# Given: an active booking and another booking in another room
# When: the booking request moving within the same room and overlapping its own time
# Expect: the move succeeds and the other booking remains unchanged
    def test_overlapping_move_in_same_room(self):
        bookings = [Booking(17, "Room 201", 600, 660),
                    Booking(18, "Room 202", 720, 780)]
        
        result = move_booking(bookings, 17, "Room 201", 630, 690)
        self.assertIs(result, bookings[0])
        self.assertEqual(result, Booking(17, "Room 201", 630, 690))
        self.assertEqual(bookings[1], Booking(18, "Room 202", 720, 780))
    

if __name__ == "__main__":
    unittest.main()

