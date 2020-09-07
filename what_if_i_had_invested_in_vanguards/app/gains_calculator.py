"""
All values based on

https://cdn.canadiancouchpotato.com/wp-content/uploads/2020/01/CCP-Model-Portfolios-Vanguard-ETFs-2019.pdf
"""

VANGUARDS_25YR_AVG_RATE_OF_RETURN = 6.38


"""
    Computes the total amount of money after a set amout of
    years usng the average rate of return

    param:average_rate_of_return assumed as a percent
"""
def calculate(current_age, retirement_age, current_money, average_rate_of_return=VANGUARDS_25YR_AVG_RATE_OF_RETURN):
    time_period = retirement_age - current_age
    result = current_money * pow(1 + (average_rate_of_return/100), time_period)
    return int(result)
