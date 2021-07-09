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
    #Invalid input is administered to by using a while loop.
    while True:
        city=input("Choose a city name between Chicago, New York City or Washington:!").lower()
        if city not in CITY_DATA:
            print("\n Not a valid city\n")
            continue
        else:
                break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
         month=str(input('Enter name of one month(from January to June) to filter by or "all" ,for no filter :')).lower()
         months=['january', 'february', 'march', 'april', 'may', 'june']
         if month == 'january':
            month = months[0]
         elif month == 'february':
              month = months[1]
         elif month == 'march':
              month = months[2]
         elif month == 'april':
             month = months[3]
         elif month == 'may':
             month = months[4]
         elif month == 'june':
             month = months[5]
         elif month == 'all':
             print('all')
         else:
              print('Invalid Input!,please restart again!.')
         break

 # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
       day=str(input('Enter name of one day to filter by or "all",for no filter:')).lower()
       days=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
       if day == 'monday':
          day = days[0]
       elif day == 'tuesday':
            day = days[1]
       elif day == 'wednesday':
            day = days[2]
       elif day == 'thursday':
            day=days[3]
       elif day == 'friday':
            day=days[4]
       elif day == 'saturday':
            day =days[5]
       elif day == 'sunday':
            day =days[6]
       elif day == 'all':
            print('all')
       else:
           print('Invalid Input!,please reatart again!.')
       break
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
    ## Loading data in DataFrame:
    df=pd.read_csv(CITY_DATA[city])
    #Converting Start-time column to data time:
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    #Extracting month from Start Time to create month column:
    df['month']=df['Start Time'].dt.month
    #Extracting day from Start Time  to create dayname column:
    df['day_of_week']=df['Start Time'].dt.weekday_name
    #Creating a new DataFrame for month:
    if month != 'all':
       months=['january', 'february', 'march', 'april', 'may', 'june']
       month=months.index(month)+1
       df=df[df['month']==month]
       #Creating a new DataFrame for dayname:
    if day != 'all':
       df=df[df['day_of_week']==day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month=pd.Series(pd.DatetimeIndex(df['Start Time'])).dt.month.mode()[0]
    print('Most common month is:',common_month)

    # TO DO: display the most common day of week
    common_day=pd.Series(pd.DatetimeIndex(df['Start Time'])).dt.day.mode()[0]
    print('Most common day is:',common_day)

    # TO DO: display the most common start hour
    common_start_hour=pd.Series(pd.DatetimeIndex(df['Start Time'])).dt.hour.mode()[0]
    print('Most common start hour is:',common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station:
    popular_start_station=df['Start Station'].mode()[0]
    print('Most commonly used start station is:',popular_start_station)

    # TO DO: display most commonly used end station:
    popular_end_station=df['End Station'].mode()[0]
    print('Most commonly used ending station is:',popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip:
    df['popular_combination_station']=df['Start Station'] + df['End Station']
    popular_combination=df['popular_combination_station'].mode()[0]
    print('Most frequent combination of Start and End Station trip:',popular_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
   ## """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time=df['Trip Duration'].sum()
    print('The total travel time is :',total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time=df['Trip Duration'].mean()
    print('The mean of travel time is :',mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types_count=df['User Type'].value_counts()
    print('count of user types:',user_types_count)

    # TO DO: Display counts of gender
    if 'Gender' in df:
        gender=df['Gender'].value_counts()
        print('The gender count is:',gender)
    else:
        print('There is no gender count data for this city')
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest=df['Birth Year'].min()
        print('The earliest Birth year is:',earliest)
        recent=df['Birth Year'].max()
        print('The recent Birth year is:',recent)
        common_birth=df['Birth Year'].mode()[0]
        print('The most common birth year is :',common_birth)
    else:
        print('There is no Birth Year data for this city.')


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
