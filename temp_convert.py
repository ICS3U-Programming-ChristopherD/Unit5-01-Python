#!/usr/bin/env python3

# Created By: Chris Di Bert
# Date: Nov. 22, 2022
# This program converts celsius to fahrenheit

def fahrenheit():

    # Gets the user's temperature in degrees celsius as a string
    temp_C_str = input("Enter the temperature in ℃ : ")

    # Tries casting the user's temperature (℃) to type float
    try:
        temp_C_float = float(temp_C_str)
    except:
        print("You must enter a number.")
    else:

        # Converts the users input (℃) to fahrenheit
        tempF = temp_C_float * 9 / 5 + 32

        # Displays the converted fahrenheit temperature
        print(f"{temp_C_str}℃ = {tempF}℉")


def main():

    # Calls the fahrenheit function
    fahrenheit()


if __name__ == "__main__":
    main()
