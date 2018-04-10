import calendar
from datetime import date


class DateDiscount:
    '''
    discount of a certain percantage applicable on a certain day
    '''

    def __init__(self, day, percentage):
        self.day = day
        self.percentage = percentage

    def is_applicable(self):
        '''
        see if discount applies
        '''
        today = date.today()
        current_day = calendar.day_name[today.weekday()]
        print(current_day)
        if self.day == current_day:
            print("discount applicable")
            return True
        else:
            print("discount not applicable")
            return False


class MultiDiscount:
    '''
    dicount of a cetrain percentage that apply when one buys a certain number of items
    '''

    def __init__(self, amount, percentage):
        pass
