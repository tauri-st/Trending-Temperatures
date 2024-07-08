import matplotlib.pyplot as plt

month = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
temp = [28,32,31,40,45,55,60,65,54,43,34,30]

plt.plot(month, temp, color="purple")

plt.xlabel("Month", fontsize=16)
plt.ylabel("Temperature", fontsize=16)

plt.title("Average Temperature in July, 2018", fontsize=20)

plt.savefig("North_Poles_Temps.png")