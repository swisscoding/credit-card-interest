#!/usr/local/bin/python3
# Made by @swisscoding on Instagram

from colored import stylize, fg

# decoration
print(stylize("\n---- | Calculate credit card interest | ----\n", fg("red")))

# class
class CCInterest:
    def __init__(self, apr, adb, days):
        self.apr = apr
        self.adb = adb
        self.days = days

    # output magic method
    def __repr__(self):
        output = stylize(self.calculation(self.apr, self.adb, self.days), fg("red"))
        return f"\nCharged credit card interest for\nthis billing cycle: {output}\n"

    # methods
    def calculation(self, apr, adb, days):
        dpr = apr / 365
        charged_interest = dpr * adb * days
        return round(charged_interest, 2)

# main execution
if __name__ == "__main__":
    # user interaction
    apr = float(input("Annual percentage rate (in %): ")) / 100
    adb = float(input("Average daily balance: "))
    days = int(input("Number of days in the billing period: "))
    print(CCInterest(apr, adb, days))
