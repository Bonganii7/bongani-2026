
import math
import matplotlib.pyplot as plt
from weighted_avg import WeightedAverage

# weights all 1's → becomes moving average filter
w = [1, 1, 1, 1, 1]  # window size n = 5 therefore we are averaging
wa = WeightedAverage(w)
"""
so the sample number represents how many points we use to represent one full sine wave cycle 
we take 200 evenly spaced points from 0 to 2pi
"""
num_samples = 200
inputs = []
outputs = []

for i in range(num_samples):
    # generate sine signal over 0 → 2π
    t = (2 * math.pi * i) / num_samples
    x = math.sin(t)
    y = wa.process(x)

    inputs.append(x)
    outputs.append(y)

# plotting
plt.figure(figsize=(10, 5))
plt.plot(inputs, label="input sine")
plt.plot(outputs, label="filtered (moving average)")
plt.title("Weighted/Moving Average Filter on Sine Wave")
plt.xlabel("sample index")
plt.ylabel("amplitude")
plt.legend()
plt.grid(True)
plt.show()
