"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are
3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23
letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in
compliance with British usage.

"""

if __name__ == '__main__':
    a = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
         11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen',
         18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty',
         70: 'seventy', 80: 'eighty', 90: 'ninety'}

    answer = 0
    for n in range(1, 1001):
        num = str(n)

        if n in a:
            answer += len(a[n])
            print(a[n])

        elif 100 > n > 20:
            tens = int(f"{str(n)[0]}0")
            units = int(str(n)[-1])
            if tens in a and units in a:
                num_as_str = f"{a[tens]}{a[units]}"
                answer += len(num_as_str)
                print(num_as_str)

        elif 1000 > n >= 100:
            hundreds = int(f"{str(n)[0]}")
            tens = int(f"{str(n)[1]}")
            units = int(str(n)[-1])

            if tens == 0 and units == 0:
                num_as_str = f"{a[hundreds]}hundred"

            elif tens == 0:
                num_as_str = f"{a[hundreds]}hundredand{a[units]}"

            elif tens == 1:
                teens = int(str(n)[1:])
                num_as_str = f"{a[hundreds]}hundredand{a[teens]}"

            else:
                tens = int(str(tens) + '0')
                if units == 0:
                    num_as_str = f"{a[hundreds]}hundredand{a[tens]}"
                else:
                    num_as_str = f"{a[hundreds]}hundredand{a[tens]}{a[units]}"

            answer += len(num_as_str)
            print(num_as_str)

        elif n == 1000:
            answer += len("onethousand")

    print(answer)