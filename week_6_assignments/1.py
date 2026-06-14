# qns 1
import math

station_name = "Kathmandu Weather Station"

temperatures = [18.4, 22.1, 15.7, 29.3, 11.8, 25.6, 19.2]


def get_average(temps):
    return sum(temps) / len(temps)


def get_deviation(temps):
    mean = get_average(temps)

    variance = 0
    for temp in temps:
        variance += (temp - mean) ** 2

    variance /= len(temps)

    return math.sqrt(variance)


def get_summary(temps):
    print(station_name)
    print("-" * 30)
    print(f"Minimum Temperature: {min(temps)}°C")
    print(f"Maximum Temperature: {max(temps)}°C")
    print(f"Average Temperature: {get_average(temps):.2f}°C")
    print(f"Standard Deviation: {get_deviation(temps):.2f}")


get_summary(temperatures)
