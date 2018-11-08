from CookingCompendium import units
from datetime import datetime
from multiprocessing import Process
import sys
import time

def spinning_cursor():
    while True:
        for cursor in '|/-\\':
            yield cursor

def run_timer(now, how_long, units):
    print(f"Running timer for {how_long} {units}.")
    spinner = spinning_cursor()
    half_printed = False
    while True:
        elapsed = (datetime.now() - now).total_seconds()
        elapsed_minutes = elapsed//60
        elapsed_hours = elapsed_minutes//60
        if units == 'seconds':
            if elapsed >= how_long:
                print("DING. Done")
                break
            if elapsed > how_long / 2:
                if not half_printed:
                    half_printed = True
                    print("Halfway there!")
        if units == 'minutes':
            if elapsed_minutes >= how_long:
                print("DING. Done")
                break
            if elapsed_minutes > how_long / 2:
                if not half_printed:
                    half_printed = True
                    print("Halfway there!")
        if units == 'hours':
            if elapsed_hours >= how_long:
                print("DING. Done")
                break
            if elapsed_hours > how_long / 2:
                if not half_printed:
                    half_printed = True
                    print("Halfway there!")
        next_spinner_item = next(spinner)
        sys.stdout.write(next_spinner_item)
        sys.stdout.flush()
        time.sleep(0.3)
        sys.stdout.write('\b')

class Base(object):
    def __init__(self, technique_name='', feeding_size=0):
        self.name = technique_name
        if units is None:
            print("'CookingCompendium.units' is not set. Defaulting to 'metric'.")
        self.units = units if units is not None else 0
        if feeding_size == 0:
            print(f"'{self.__class__.__name__}.feeding_size' is not set. Defaulting to 2. Your mom said you should get married soon.\n\n\tJust sayin...")
            self.feeding_size = 2
        else:
            self.feeding_size = feeding_size

    def set_feeding_size(self, number_of_people):
        if number_of_people > 0:
            self.feeding_size = number_of_people
        if number_of_people < 2:
            return "How selfish..."

    def show_ingredients(self):
        try:
            getattr(self, 'ingredients')
            print(self.ingredients)
        except:
            print(".ingredients not set")

    def __convert(self, amount, div_by, decimal_places=2):
        return round(amount / div_by, decimal_places)

    def __pounds_to_kilograms__(self, pounds):
        return self.__convert(pounds, 2.205)

    def __cups_to_liters__(self, cups):
        return self.__convert(cups, 4.227)
    
    def __repr__(self):
        return "%s" % (self.name, )

    class Timer(object):
        def set_timer(self, how_long, units):
            now = datetime.now()
            p = Process(target=run_timer, args=(now, how_long, units))
            p.start()
            p.join()

