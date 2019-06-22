# Python program to find the number of days between input dates
# Dates to be entered in dd-mm-yyyy format
# WIll approach the crude way - number of days in a month. No standard python libraries used

def date_preceding_zero_remove(input_date):
    return input_date[0:len(from_date)]

def days_between_dates_of_same_year(from_date_input, to_date_input):
    dict_month_days = {
        '1': '31',
        '2': '28',
        '3': '31',
        '4': '30',
        '5': '31',
        '6': '30',
        '7': '31',
        '8': '31',
        '9': '30',
        '10': '31',
        '11': '30',
        '12': '31'
    }

    month_arr = []
    from_date = from_date_input.split('-')
    to_date = to_date_input.split('-')

    [month_arr.append(key) for key in dict_month_days.keys()]
    selected_month_arr = month_arr[int(from_date[1]): int(to_date[1])-1]

    if len(selected_month_arr) != 0:
        number_of_days_months = 0
        for month in selected_month_arr:
            number_of_days_months += int(dict_month_days[month])
    else:
        number_of_days_months = 0

    number_of_days_of_from_month = int(dict_month_days[(from_date[1]).lstrip('0')]) - int(from_date[0].lstrip('0'))
    number_of_days_of_to_month = int(to_date[0].lstrip('0'))

    total_days = number_of_days_months + number_of_days_of_from_month + number_of_days_of_to_month
    total_weeks = int(total_days/7)
    return total_days, total_weeks

def number_of_days_between_two_dates(from_date_input, to_date_input):

   # Creating a leap year array from year 0 to year 10000!!!
    leap_year = []
    total = 0
    [leap_year.append(y) for y in range(0,10000,4)]

    from_date = from_date_input.split('-')
    to_date = to_date_input.split('-')
    year_diff = int(to_date[2]) - int(from_date[2])

    if year_diff > 1:
        # To find out all the years between input dates
        years_between = []
        [years_between.append(year) for year in range(int(from_date[2]), int(to_date[2]))]
        years_between.pop(0)

        # To find out sum of all days of all the years between input dates
        number_of_days_between_years_excluding_input_years = 0
        for year in years_between:
            if year in leap_year:
                print("Year is %s" %year)
                number_of_days_between_years_excluding_input_years += 366
            else :
                number_of_days_between_years_excluding_input_years += 365

        number_of_days_from_year = days_between_dates_of_same_year(from_date_input, '31-12-' + from_date[2])
        number_of_days_to_year = days_between_dates_of_same_year('1-1-' + to_date[2], to_date_input)
        total = number_of_days_between_years_excluding_input_years + number_of_days_from_year[0] + \
                number_of_days_to_year[0]

    elif year_diff == 1:
        number_of_days_from_year = days_between_dates_of_same_year(from_date_input, '31-12-'+ from_date[2])
        number_of_days_to_year = days_between_dates_of_same_year('1-1-'+to_date[2], to_date_input)
        total =  number_of_days_from_year[0] + number_of_days_to_year[0]
    elif year_diff == 0:
        total = days_between_dates_of_same_year(from_date_input, to_date_input)
        total = total[0]

    print("Total days between %s & %s is %s" %(from_date_input, to_date_input, total))


if __name__ == '__main__':
    from_date = input("Enter from date in dd-mm-yyyy format")
    to_date = input("Enter to  date in dd-mm-yyyy format")

    number_of_days_between_two_dates(from_date, to_date)