import time
import pandas as pd
import numpy as np

#input city names
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
    city = input('Would you like to see data for Chicago, New York City, Washington?').lower()

    print(city)

    while city not in ['chicago','washington','new york city']:
        city = input('Input available name of the city').lower()
        continue


    # TO DO: get user input for month (all, january, february, ... , june)

    month = input('choose month from January, Febraury, March, April, May, June or all').lower()
    while month not in ['january','febraury','march','april','may','june','all'] :
        month = input('Please input available month name')
        continue
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    day = input('choose day of week or all').lower()
    while day not in ['sunday','monday','tuesday','wednesday','thursday','friday','saturday', 'all']:
        day = input('please input day of week')

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
# sub program to display raw data

    filename = ("{}.csv".format(city.replace(" ","_")))
    print(filename)
    df = pd.read_csv(filename)


    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'all':
        months = ['january', 'febraury', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]



    if day != 'all':
        df = df[df['day_of_week'] == day.title()]



    question = input("Type \"yes\" if you would like to see raw data or type \"no\" to continue").lower()

    x = 0
    y = 5
    while question not in ["no","yes"]:

        question = input("Please check for error in input")
        continue
    while question not in ["no"]:
        out_put = df.iloc[x:y,:]
        print(out_put)
        question = input("Type \"yes\" if you would like to see more or \"no\" to continue")
        x = y
        y += 5
        continue
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode().values[0]
    print('most popular month: {} '.format(popular_month))

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode().values[0]
    print('most popular day_of_week: {} '.format(popular_day))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode().values[0]
    print('most popular hour: {}'.format(popular_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode().values[0]
    print('Popular start station: {} '.format(popular_start_station))

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode().values[0]
    print('\npopular end station: {} '.format(popular_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    counts = df.groupby(['Start Station','End Station']).size().idxmax()
    print('\nMost frequent combination {}'.format(str(counts)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    df['End Time'] = pd.to_datetime(df['End Time'])


    df['Duration'] = df['End Time'] - df['Start Time']



    # TO DO: display total travel time

    print('total time travel:',(df['Duration'].sum()))

    # TO DO: display mean travel time
    print('mean travel time: ',(df['Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""


    print('\nCalculating User Stats...\n')
    start_time = time.time()

    user_types = df['User Type'].value_counts()
    print('\nCounts of User types:\n {} '.format(user_types))


    # TO DO: Display counts of gender
    try:

        Gender = df['Gender'].value_counts()
        print('\nCounts of gender:\n {}'.format(Gender))
    except:

        print(" Sorry Gender information is not available for the city")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_num = df['Birth Year'].min()
        print('\nEarliest birthday: {}'.format(int(earliest_num)))

        recent_num = df['Birth Year'].max()
        print('\nRecent birthday: {} '.format(int(recent_num)))

        common_year = df['Birth Year'].mode()
        print('\nCommon year of birthday: {} '.format(int(common_year)))
    except:
        print("Sorry information is not available for the city")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)





    # TO DO: Display counts of user types



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
