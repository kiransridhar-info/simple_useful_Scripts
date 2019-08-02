# GUI program to take inputs dates from user and calculate the number of days between
# Do not select below year 2000 as tkcalender does not work correctly
# Purposely did not use many libraries for some "brute" self practise

import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar, DateEntry

# Creating a leap year array from year 0 to year 10000!!!
leap_year = []
total = 0
[leap_year.append(y) for y in range(0, 10000, 4)]

def definitions(from_date_tk, to_date_tk):
    print ("TO FIND DAYS BETWEEN %s AND %s" %(from_date_tk, to_date_tk))
    from_date_tk = str(from_date_tk)
    to_date_tk = str(to_date_tk)
    from_date_tk = from_date_tk.split("-")[2] + "-" + from_date_tk.split("-")[1] + "-" + from_date_tk.split("-")[0]
    to_date_tk = to_date_tk.split("-")[2] + "-" + to_date_tk.split("-")[1] + "-" + to_date_tk.split("-")[0]
    totalDays = number_of_days_between_two_dates(from_date_tk, to_date_tk)
    print("Total number of days from definitions%s" % totalDays)
    return totalDays

def dateentry_view():
    def print_sel():
        val_entry_date = (cal.get_date())
        val_entry_date1 = (cal1.get_date())
        totalDays = definitions(val_entry_date,val_entry_date1)
        result = tk.Label(top, text='NUMBER OF DAYS :')
        result.pack(padx=10, pady=10)
        result["text"] = 'NUMBER OF DAYS :' + str(totalDays)
        print("Total number of days %s " %totalDays)

    top = tk.Toplevel(root)

    tk.Label(top, text='Choose date').pack(padx=10, pady=10)
    cal = DateEntry(top, width=12, background='darkblue',foreground='white', borderwidth=2, dateformat = 3)
    cal1 = DateEntry(top, width=12, background='darkblue', foreground='white', borderwidth=2,  dateformat = 3)
    cal.pack(padx=10, pady=10)
    cal1.pack(padx=12, pady=10)
    tk.Button(top, text="ok", command=print_sel).pack()

def validate_date(input_date):
    months_with_thirty_days = ['4','6','9','10','9','11']
    months_with_thirtyOne_days = ['1','3','5','7','8','10','12']

    if len(input_date[0]) == 1 or len(input_date[0]) == 2 and len(input_date[1]) == 1 or len(input_date[1]) == 2 and \
            len(input_date[2]) == 4:
        if input_date[0].isdigit() and input_date[1].isdigit() and input_date[2].isdigit():

            if input_date[1] == '2' and int(input_date[0]) > 28:
                if input_date[2] not in leap_year:
                    raise ValueError ("Not a valid date as it is not a leap year and Feb is input with 29 days")
            elif input_date[1] == '2' and int(input_date[0]) > 29:
                if input_date[2] in leap_year:
                    raise ValueError("Not a valid date as it is more than 29 days for Feb")

            if int(input_date[1]) > 12:
                raise ValueError("Not a valid date as month value is more than 12")
            else :
                if input_date[1] in months_with_thirty_days:
                    if int(input_date[0]) > 30:
                        raise ValueError("Not a valid date as number of days is more than 30 for even months")
                elif input_date[1] in months_with_thirtyOne_days:
                    if int(input_date[0]) > 31:
                        raise ValueError("Not a valid date as number of days is more than 31 for odd months")
        else :
            raise ValueError("Input date not having numbers. Correct the same")
    else:
        raise ValueError("Input date not having right number of digits. Please correct the same")

    return 'Valid_Date'


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

    print ("test %s %s" %(from_date_input, to_date_input))
    month_arr = []
    from_date = from_date_input.split('-')
    to_date = to_date_input.split('-')
    from_date = [x.lstrip('0') for x in from_date]
    to_date = [x.lstrip('0') for x in to_date]

    print("both dates" ,from_date,to_date)
    [month_arr.append(key) for key in dict_month_days.keys()]
    selected_month_arr = month_arr[int(from_date[1]): int(to_date[1])-1]

    if int(from_date[1]) > int(to_date[1]):
        raise ValueError("From date is more than To Date")

    if from_date == to_date:
        total_days = 0
        total_weeks = 0
        return total_days, total_weeks

    if from_date[2] == to_date[2] and from_date[1] == to_date[1]:
        total_days = int(to_date[0]) - int(from_date[0])
        if total_days > 0:
            total_weeks = int(total_days/7)
            return total_days, total_weeks
        else:
            raise ValueError("From date is more than To Date")

    if len(selected_month_arr) != 0:
        number_of_days_months = 0
        for month in selected_month_arr:
            number_of_days_months += int(dict_month_days[month])
    else:
        number_of_days_months = 0

    number_of_days_of_from_month = int(dict_month_days[(from_date[1])]) - int(from_date[0])
    number_of_days_of_to_month = int(to_date[0])

    total_days = number_of_days_months + number_of_days_of_from_month + number_of_days_of_to_month
    print("all", number_of_days_months, number_of_days_of_from_month ,number_of_days_of_to_month)
    total_weeks = int(total_days/7)
    return total_days, total_weeks

def number_of_days_between_two_dates(from_date_input, to_date_input):

    from_date = str(from_date_input)
    to_date = str(to_date_input)

    from_date = from_date.split('-')
    to_date = to_date.split('-')

    from_date = [x.lstrip('0') for x in from_date]
    to_date = [x.lstrip('0') for x in to_date]

    if (validate_date(from_date)) != 'Valid_Date' or (validate_date(to_date)) != 'Valid_Date':
        raise ValueError("Ensure the date input is valid")
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
                print("Leap Year is %s" %year)
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

    return total

if __name__ == '__main__':
    root = tk.Tk()
    root.title('Number of days calculator')
    s = ttk.Style(root)
    s.theme_use('clam')
    ttk.Button(root, text='Click to enter dates', command=dateentry_view).pack(padx=10, pady=10)
    root.mainloop()