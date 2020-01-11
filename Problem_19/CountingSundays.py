"""

You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.

A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

"""

days = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']
months = {'Enero': 31, 'Febrero': 28, 'Marzo': 31, 'April': 30, 'Mayo': 31, 'Junio': 30,
          'Julio': 31, 'Agosto': 31, 'Septiembre': 30, 'Octobre': 31, 'Noviembre': 30, 'Diciembre': 31}


def loop_through_days(indx, how_many_days):
    new_index = indx + how_many_days
    while new_index > 6:
        new_index -= 7
    return new_index


def go():
    day_index = 0
    count_sundays = 0

    for year in range(1900, 2001):
        if year != 1900 and not year % 4:
            print(f"{year}*")
            daysinyear = 366
        else:
            print(f"{year}")
            daysinyear = 365

        m = day_index

        if year > 1900:
            for k, v in months.items():
                if daysinyear == 366 and v == 28:
                    v = 29

                if m == 6:
                    count_sundays += 1
                    print(f"\t{k:<12} ->  {days[m]} ** ({count_sundays})")
                else:
                    print(f"\t{k:<12} ->  {days[m]}")

                m = loop_through_days(m, v)

        day_index = loop_through_days(day_index, daysinyear % 7)
        print()

    return count_sundays


if __name__ == '__main__':
    answer = go()
    print(f'Answer: {answer}')
