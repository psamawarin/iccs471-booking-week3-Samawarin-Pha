## Identity: 
- Name: Samawarin Phakdeewanit
- Student ID: 6681338
- AI tool use 
- Worked independently


## Review decision 
Approve 'move_booking' implementation. It checks conflict and validates incoming request before moving a booking. After a move, it only changes room, start and end.

### Checks
- Command: uv run --python 3.12 python -m unittest -v test_baseline test_move_smoke test_student
- Expected: **11 tests, OK**
- baseline commit ID: 09ce957e336380fc05958050ccd333096d6c4481

### Remaining uncertainty
The tests do not verify if moving a cancelled target raises a ValueError or just leaves record unchanged.
