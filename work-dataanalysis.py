# Data Analysis
# Author: Princeton Vuong
#

# Analyse the data provided in class


def rain():
    path = "data/NYC_Central_Park_weather_1869-2022.csv"
    file = open(path)

    count = 0
    total_rain = 0
    total_tmin = 0
    total_tmax_june = 0
    count_june = 0

    file.readline()

    for line in file:
        line = line.strip()
        DATE, PRCP, SNOW, SNWD, TMIN, TMAX = line.split(",")

        if PRCP == "" or TMIN == "" or TMAX == "":
            continue

        parts = DATE.split("-")
        month = parts[1]  # no slicing needed

        prcp = float(PRCP)
        tmin = float(TMIN)
        tmax = float(TMAX)

        count = count + 1
        total_rain = total_rain + prcp
        total_tmin = total_tmin + tmin

        if month == "06":
            total_tmax_june = total_tmax_june + tmax
            count_june = count_june + 1

    file.close()

    avg_rain = total_rain / count
    avg_tmin_f = total_tmin / count
    avg_tmin_c = (avg_tmin_f - 32) * 5 / 9
    avg_tmax_june = total_tmax_june / count_june

    print("Number of data points:", count)
    print("Average rainfall:", avg_rain)
    print("Average minimum temp (F):", avg_tmin_f)
    print("Average minimum temp (C):", avg_tmin_c)
    print("Average June maximum temp (F):", avg_tmax_june)


if __name__ == "__main__":
    rain()
