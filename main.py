from SenecSim.UniteData import read_momentary_values, read_timespan_values
from matplotlib import pyplot as plt


momentary_values = read_momentary_values()
timespan_values = read_timespan_values()

momentary_values.sort()
timespan_values.sort()

for value in momentary_values:
    print(value.timestamp)



# times = [value.timestamp for value in momentary_values]
# socs = [value.soc for value in momentary_values]
# plt.plot(times, socs)
# plt.show()
