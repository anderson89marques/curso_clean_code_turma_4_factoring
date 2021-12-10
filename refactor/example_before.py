# calculate ride
def calc(dist, d):

    # overnight

    if d.hour >= 22:

        return dist * 3.90
    else:
        # sunday
        if d.day == 0:

            return dist * 2.9
        else:
            return dist * 2.10
