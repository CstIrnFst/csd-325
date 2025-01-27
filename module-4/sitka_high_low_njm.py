# Nathan Maurer
# January 26, 2025
# Module 4.2 Assignment

import csv  # allows reading of csv files
from datetime import datetime  # date and time displaying module
from matplotlib import pyplot as plt  # functions to create plots

class TempPlot:     # create class used by either user input class (Highs or Lows)

    def __init__(self, filename,temp_index, title):  # constructor to initialize object
        self.filename = filename  # object attributes (initialized)
        self.temp_index = temp_index
        self.title = title

    def plot(self): # defines the plot object
        with open(self.filename) as f:  # f = filename
            reader = csv.reader(f)  # opens csv filetype reader
            header_row = next(reader)

            dates,temps = [], []
            for row in reader:
                current_date = datetime.strptime(row[2], '%Y-%m-%d')  # removes the time, retains y/m/d in original format
                dates.append(current_date)  # allows change of date
                temps.append(int(row[self.temp_index]))  # allows change of temp based on date/time data

            fig, ax = plt.subplots()
            ax.plot(dates,temps, c = 'blue')    # plot x = dates, y = temps, in blue

            plt.title(self.title, fontsize=24)          #  Plot formatting and font sizes
            plt.xlabel("Date - Year/Month", fontsize = 14)
            fig.autofmt_xdate()
            plt.ylabel("Temperature (F)", fontsize = 14)
            plt.tick_params(axis= 'both', which = 'major', labelsize = 14)
            plt.show()

def main():
    user_input = input("Type 'Highs' to see historical high temperatures. Type 'Lows' to see historical low temperatures.  Type 'Exit' to exit. Do you want to see 'Highs' or 'Lows': ")

    class_map = {
            'Highs':TempPlot('sitka_weather_2018_simple.csv', 5, "Daily High Temperatures - 2018"), # two classes, filename, temp_index, and title from initialization
            'Lows':TempPlot('sitka_weather_2018_simple.csv', 6, "Daily Low Temperatures - 2018")
    }    # creates a class map of both possible selections, Highs and Lows

    if user_input in class_map:     # selects class based on user input
        selected_class = class_map[user_input]
        selected_class.plot()

        main()      # loop back through program if not exited

    elif user_input:    # exits if user selects 'exit'
        selected_class = exit
        print("Exited")

    else:   # prints invalid if user input is not recognized
        print("Invalid response")

if __name__ == "__main__":
    main()