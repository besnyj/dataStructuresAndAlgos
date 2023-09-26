# this is the example of a fibonacci function but the application is almost the same for every problem.
# set the baselines, and then apply all of the rest.

def num_ways(n):
    if n == 0 or n == 1:
        return 1

    bottom_up = [0]*(n+1)

    bottom_up[0] = 1
    bottom_up[1] = 1

    for i in range(2, n+1):
        bottom_up[i] = bottom_up[i-1]+bottom_up[i-2]
    print(bottom_up)

    return bottom_up[n]
