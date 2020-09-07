"""
All values based on

https://help.wealthsimple.com/hc/en-ca/articles/214187018-How-has-the-Growth-portfolio-performed-
"""

WEALTHSIMPLE_AVG_RATE_OF_RETURN = 7.3


"""
    Computes the total amount of money after a set amout of
    years usng the average rate of return

    param:average_rate_of_return assumed as a percent
"""
def calculate(current_age, retirement_age, current_money, average_rate_of_return=WEALTHSIMPLE_AVG_RATE_OF_RETURN):
    time_period = retirement_age - current_age
    result = current_money * pow(1 + (average_rate_of_return/100), time_period)
    return int(result)
