def odometer(oksana):
    distance = 0
    distance += oksana[0] * oksana[1]
    if len(oksana) > 2:
        for i in range(2, len(oksana) - 1, 2):
            previous = oksana[i - 1]
            distance += oksana[i] * (oksana[i + 1] - previous)
    return distance