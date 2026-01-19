# Nathan Maurer
# January 18, 2026
# Module 4.2 Assignment


import csv  # for reading csv files
from datetime import datetime
from platform import java_ver   # for manipulating dates
from matplotlib import pyplot as plt  # Creates plots

class TempPlot:   # create class used by High or Low input class
    def __init__(self, filename, temp_index, title):  # Constructor initializes object
        self.filename = filename
        self.temp_index = temp_index
        self.title = title

    def plot(self):  # defines Plot object
        with open(self.filename) as f:  # f = filename
            reader = csv.reader(f)  # opens csv filetype reader
            header_row = next(reader)

            dates, temps = [], []
            for row in reader:
                current_date = datetime.strptime(row[2], '%Y-%m-%d')  # removes time, retains y/m/d format
                dates.append(current_date)  # allows changing of the date
                temp = int(row[self.temp_index])
                temps.append(int(row[self.temp_index]))  # can change temp based on date/time

            fig, ax = plt.subplots()  # creates figure and axis objects
            ax.plot(dates, temps, c='blue')  # plots dates and temps in blue

            plt.title(self.title, fontsize=24)  # title of plot
            plt.xlabel("Date - Year/Month", fontsize = 14)  # x-axis label
            fig.autofmt_xdate()  # formats x-axis date
            plt.ylabel("Temperature (F)", fontsize=14)  # y-axis label
            plt.tick_params(axis='both', which='major', labelsize=14)  # tick parameters
            plt.show()  # shows plot

def main():
    user_input = input("Type 'Highs' or 'Lows' to see historical data. Type 'Exit' to quit. Do you want to see 'Highs' or 'Lows'?: ")
    
    class_map = {
        'Highs': TempPlot('sitka_weather_2018_simple.csv', 5, "Daily high temperatures - 2018"),
        'Lows': TempPlot('sitka_weather_2018_simple.csv', 6, "Daily low temperatures - 2018")
    }  # creates class map for user input

    if user_input in class_map:  # selects class based on user input
        selected_class = class_map[user_input]
        selected_class.plot()

        main()  # loop back if not exited

    elif user_input:  # Exits if user chooses
        selected_class = exit
        print ("Exited")

    else:       # prints invalid if input not recognized
        print ("Invalid response")

if __name__ == "__main__":
    main()