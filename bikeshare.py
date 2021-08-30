import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    #Welcome message
    print('Hello! Let\'s explore some US bikeshare data!\n')

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs



    #Creting a while loop to handel invalid inputs.
    while True:

        #Asking the user to input the city they want to perform analysis on
        city = input('Would you like to see data for Chicago, New york, or Washington?\n(Pleas write the city names as they are written in the qustion)\n').lower()

        #Create a cindition statment to check if the user input is correct
        if city in CITY_DATA:

            break

        #Error massege tha appears when the user enter inccorrect value
        else:
            print('You have interd an invalid input please check your previous input and try again!\n')


    # get user input for month (all, january, february, ... , june)

    #Create a list to store the months
    months = ['January', 'February','March', 'April',
                'May','June', 'all']

    #Creting a while loop to handel invalid inputs.
    while True:

        #Ask the user whethere they want to filter by a specific month or all
        month = input('\nWould you like to filter by a specific month (from the first six months only) or all?\nIf by a specifc month write the name of the month,else write "all"\n')

        #Create a cindition statment to check if the user input is correct

        if month in months:

            break

        #Error massege tha appears when the user enter inccorrect value
        else:
            print('You have interd an invalid input please check your previous input and try again!\n')


    #get user input for day of week (all, monday, tuesday, ... sunday)

    #Create a list to store the days of the week
    week_days = ['Sunday', 'Monday','Tuesday', 'Wednesday',
                 'Thursday', 'Friday', 'Saturday', 'all']

    #Creting a while loop to handel invalid inputs.
    while True:

        #Asking the user to input the day they want to perform analysis on
        day = input('\nWould you like to filter by a specific day or all?\nIf by a specifc day write the name of the day,else write "all"\n')

        # Create a cindition statment to check if the user input is correct
        if day in week_days:

                break

        #Error massege tha appears when the user enter inccorrect value
        else:
            print('You have interd an invalid input please check your previous input and try again!\n')


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

    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()



    # display the most common month
    print('\nMost Common month:', df['month'].mode()[0])


    # display the most common day of week
    print('\n\nMost Commen Day Of The Week:', df['day_of_week'].mode()[0])

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour


    # display the most common start hour
    print('\n\nMost Commen Start Hour:', df['hour'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # find the most commonly used start station
    common_start_station = df['Start Station'].mode()[0]

    # display most commonly used start station
    print('\nMost Common Start Station:', common_start_station)

    # find the most commonly used end station
    common_end_station = df['End Station'].mode()[0]

    # display most commonly used end station
    print('\n\nMost Common End Station:', common_end_station)

    # find the most frequent combination of start station and end station trip
    common_stations = ('\n Start Station: '+df['Start Station']+'\n End Station: '+ df['End Station']).mode()[0]

    # display most
    print('\n\nMost Frequent Combination Of Start And End Station Trip:-', common_stations)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # calculate total travel time
    total_travel_time = df['Trip Duration'].sum()

    # display total travel time
    print('\nTotal Time Travel In Seconds:', total_travel_time )

    # calculate mean travel time
    mean_travel_time = df['Trip Duration'].mean()

    # display mean travel time
    print('\nMean Travel Time:', mean_travel_time )


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Calculate the counts of each user type
    users_count = df['User Type'].value_counts().to_string()

    # Display counts of user types
    print('\nCount Of Each User Type:\n',users_count)


    #Condition staments to only display the gender information if the cities are Chicago and New York.

    if city != 'washington':

        # Calculate counts of gender
        gender_count = df['Gender'].value_counts().to_string()

        # Display counts of gender
        print('\nCount Of Each Gender:\n',gender_count)

        # Calculate the earliest, most recent, and most common year of birth
        earliest_birth_year = df['Birth Year'].min()

        recent_birth_year = df['Birth Year'].max()

        common_birth_year = df['Birth Year'].mode()[0]

        # Display earliest, most recent, and most common year of birth
        print('\nEarliest Year Of Birth:',earliest_birth_year)

        print('\nMost Recent Year Of Birth:',recent_birth_year)

        print('\nMost Common Year Of Birth:',common_birth_year)



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)

        #ask the user wethere they would like to see the raw data
        rawdata_input = input('\nWould you like to see the raw data? Enter yes or no. \n')


        #while loop and if statment to show the raw data or not

        #intialiaze variable that acts as a counter to show raw data

        rawdata_counter = 5

        while True:

            if rawdata_input != 'yes':
                break

            elif rawdata_input == 'yes':
                print(df.head(rawdata_counter))

                more_rawdata = input('\nWould you like to see more raw data? Enter yes or no. \n')

                if more_rawdata != 'yes':
                    break

                elif more_rawdata == 'yes':

                    rawdata_counter += 5

                    print(df.head(rawdata_counter))


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
