"""Booking operations. Implement only the agreed rescheduling change."""
from models import Booking
from rules import validate_room, validate_interval, has_conflict

def find_booking(bookings: list[Booking], booking_id: int) -> Booking:
    for booking in bookings:
        if booking.id == booking_id:
            return booking
    raise ValueError("Booking not found")

def add_booking(bookings: list[Booking], room: str, start: int, end: int) -> Booking:
    validate_room(room)
    validate_interval(start, end)
    if has_conflict(bookings, room, start, end):
        raise ValueError("Booking conflict")
    next_id = max((booking.id for booking in bookings), default=0) + 1
    booking = Booking(next_id, room, start, end)
    bookings.append(booking)
    return booking

def move_booking(bookings: list[Booking], booking_id: int, new_room: str,
                 new_start: int, new_end: int) -> Booking:
    booking = find_booking(bookings, booking_id)
    if booking.status != "active":
        raise ValueError("Cannot move a cancelled booking")

    validate_room(new_room)
    validate_interval(new_start, new_end)
    if any(
        other is not booking
        and other.status == "active"
        and other.room == new_room
        and new_start < other.end
        and other.start < new_end
        for other in bookings
    ):
        raise ValueError("Booking conflict")

    booking.room = new_room
    booking.start = new_start
    booking.end = new_end
    return booking
