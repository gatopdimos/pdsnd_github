import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTH_DATA = {"January":1, "February":2, "March":3, "April":4, "May":5, "June":6, "July":7, "August":8, "September":9, "October":10, "November":11, "December":12}

WEEKDAY_DATA = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    while True:
        city_user_input = input("From the defined list of cities (Chicago, New York City, Washington) type the name of the one you wish to analyze: ")
        # remove white spaces and change the user input value to lowercase
        city_lower_case = city_user_input.strip().lower()
        if city_lower_case in CITY_DATA:
            city = city_lower_case
            break
        else:
            print("Warning: The city provided does not exist in our dataset. In the follow up request, please provide a city name that exists in our dataset such as Chicago, New York City or Washington.\n")

    # TO DO: get user input for month (all, january, february, ... , june)
    
    while True:
        month_user_input = input("Please type the name of the month for which you wish to view data for (e.g. May) if you explicitely want to see data of a specific month. Alternatively, type 'All' to have all months in the end result:\n")
        # remove white spaces and change the user input value to lowercase
        month_title = month_user_input.strip().title()
        if month_title in MONTH_DATA:
            month = month_title
            break
        elif month_title == "All":
            month = "all"
            break
        else:
            print("Warning: The value provided for month is not correct. Please type the name of the month for which you wish to view data for (e.g. May) or type 'All' to have all months in the end result.\n")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
        week_day_user_input = input("Please type the name of the day of the week for which you wish to view data for (e.g. Monday) if you explicitely want to see data of a specifc day of the week. Alternatively, type 'All' to have all days of the week in the end result:\n")
        week_day_title = week_day_user_input.strip().title()
        if week_day_title in WEEKDAY_DATA:
            day = week_day_title
            break
        elif week_day_title == "All":
            day = "all"
            break
        else:
            print("Warning: The value provided for the day of the week is not correct. Please type the name of the day of the week for which you wish to view data for (e.g. Monday).Alternatively, type 'All' to have all days of the week in the end result.\n")
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    #create a new column with the month name to be used for plotting
    df['month_name'] = df['Start Time'].dt.month_name()
    # filter by month if applicable
    if month != "all":
        month_number = MONTH_DATA[month]
        df = df[df['month'] == month_number]
    # filter by day of the week if applicable
    if day != "all":
        df = df[df['day_of_week'] == day]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("The most common month is: ",df['month_name'].mode()[0])

    # TO DO: display the most common day of week
    print("The most common day of weeek is: ",df['day_of_week'].mode()[0])

    # TO DO: display the most common start hour
    print("The most common start hour is: ", df['Start Time'].dt.hour.mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("The most commonly used start station is: ", df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print("The most commonly used end station is: ", df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    most_popular_destination = df.groupby(by=["Start Station","End Station"]).size().idxmax()
    print(f"The most frequent combination of start station and end station trip is: Start Station: {most_popular_destination[0]} , End Station: {most_popular_destination[1]}.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time


    # display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types


    # Display counts of gender


    # Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
