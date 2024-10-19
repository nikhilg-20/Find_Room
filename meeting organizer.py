def findMinRooms(*meetings):
    try:
        if not all(isinstance(meeting, list) and len(meeting) == 2 and isinstance(meeting[0], (int, float)) and isinstance(meeting[1], (int, float)) for meeting in meetings):
            raise ValueError("The start time and end time of every meeting must be given in two integers.")

        # Separate and sort the start and end times
        start_times = sorted(meeting[0] for meeting in meetings)
        end_times = sorted(meeting[1] for meeting in meetings)

        # Organize arrows to help you travel between the start and end times.
        start_ptr = 0
        end_ptr = 0
        rooms_needed = 0
        max_rooms = 0

        while start_ptr < len(start_times):
            if start_times[start_ptr] < end_times[end_ptr]:
                rooms_needed += 1
                start_ptr += 1
                max_rooms = max(max_rooms, rooms_needed)  # Keep tabs on the most rooms that are in use.
            else:
                # The meeting is over, clearing the space.
                rooms_needed -= 1
                end_ptr += 1

        return max_rooms

    except ValueError as e:
        print(f"Input error: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None