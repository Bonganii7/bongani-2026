from collections import deque
from typing import List, Optional


class WeightedAverage:
    def __init__(self, w: List[float]):
        """
        as noted from given interface, initialize with weights. and the length of w will determine n
        """
        self.w = w
        self.n = len(w)
        # stores last n samples, index 0 must be newest
        self.x = deque(maxlen=self.n)

    def process(self, sample: float) -> Optional[float]:
        """
        now passing the process method the aim is to insert new value x
        and return weighted average of last n samples.
        Returns None until at least n samples have been collected.
        """

        self.x.appendleft(sample)

        if len(self.x) < self.n:
            return None

        total = 0.0
        for i in range(self.n):
            total += self.w[i] * self.x[i]
        return  total / self.n

       # for weight, value in zip(self.weights, self.window):
       #     total += weight * value

        # divide by n exactly as specification example shows
        #return total / self.n




