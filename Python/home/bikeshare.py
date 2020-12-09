import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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
        city = input("input for city (chicago, new york city, washington): ").lower()
        if city in ('chicago','new york city', 'washington'):
            break
        else:
            print("Invalid input. Please try again")

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input ("input for month (all, january, february, ... , june): ").lower()
        if month in ('all','januray','february','march','april','may','june'):
            break
        else:
            print("Invalid input. Please try again")
    

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("input for day of week (all, monday, tuesday, ... sunday): ").lower()
        if day in ('all','monday','tuesday','wednesday','thursday','friday','saturday','sunday'):
            break
        else:
            print("Invalid input. Please try again")
    

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
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
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

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    most_common_month_count = df['month'].value_counts().max()
    print('The most common month: {}. Count:{} '.format(most_common_month,most_common_month_count))

    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    most_common_day_count = df['day_of_week'].value_counts().max()
    print('The most common day of the week: {}. Count: {} '.format(most_common_day,most_common_day_count))

    # TO DO: display the most common start hour
    most_common_hour = df['hour'].mode()[0]
    most_common_hour_count = df['hour'].value_counts().max()
    print('The most common start hour: {}. Count: {}'.format(most_common_hour,most_common_hour_count ))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print('most commonly used start station: {}'.format(most_common_start_station))
    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print('most commonly used end station: {}'.format(most_common_end_station))
    # TO DO: display most frequent combination of start station and end station trip
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('total travel time: {}'.format(total_travel_time))
    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('mean travel time: {}'.format(mean_travel_time))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    counts_user_types = df['User Type'].count()
    print('counts of user types: {}'.format(counts_user_types))
    # TO DO: Display counts of gender
    try:
        counts_of_gender = df['Gender'].count()
        print('counts of gender: {}'.format(counts_of_gender))
    except KeyError:
        print('No Gender Data Available')
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_year_of_birth = df['Birth Year'].min()
        most_recent_year_of_birth = df['Birth Year'].max()
        most_common_year_of_birth = df['Birth Year'].mode()[0]
        print('earliest, most recent, and most common year of birth: {} , {}, {}'.format(earliest_year_of_birth,most_recent_year_of_birth,most_common_year_of_birth))
    except KeyError:
        print('No Birth Year Data Available')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def display(df):
    times = 0
    while True:
        display = input ('\ndo you want to display raw data? yes or no\n')
        times += 5
        if display.lower() == 'yes':
            print(df.head(times))
        else: break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display(df)
        
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

            
            
            


if __name__ == "__main__":
    main()
