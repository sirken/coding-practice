'''
Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
'''


def check_rooms(rooms):
    # Make full list to get max, min times
    t = []
    for r in rooms:
        t.extend(r)

    # Loop through time range
    total_rooms = 0
    counter = 0
    for x in range(min(t), max(t)+1):
        if x in t:
            if t.index(x) % 2 == 0:
                counter += 1
                if total_rooms < counter:
                    total_rooms = counter
            else:
                counter -= 1
    return total_rooms

print(check_rooms([(30, 75), (0, 50), (60, 150)]))