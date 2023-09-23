

def min_days(durations):
    durations.sort()
    days = 0
    left = 0
    right = len(durations) - 1

    while left <= right:
        days += 1

        if durations[left] + durations[right] <= 3.0:
            left += 1
            right -= 1
        else:
            right -= 1

    return days


d1 = [1.90, 1.04, 1.25, 2.5, 1.75]
d2 = [1.01, 1.01, 1.01, 1.4, 2.4]
d3 = [1.01, 1.991, 1.32, 1.4]

print(min_days(d1))
print(min_days(d2))
print(min_days(d3))
