from weighted_avg import WeightedAverage

wa = WeightedAverage([5,4,3,2,1])# the newest w[0] = 5 and the oldest w[4] = 1 and used the y[n] formula


for s in [5,4,3,2,1]: # after 5 updates we have x[0] newest value = 1 and x[1] = 2 older and so on.
    print(wa.process(s))