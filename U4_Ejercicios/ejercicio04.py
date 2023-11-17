from datetime import date   
from datetime import datetime
import dateutil.relativedelta  as rdelta


class GestFechas:
    @staticmethod
    def getOldDate(*manydates):
        my_dates = sorted(manydates)
        return my_dates[0]
    
    @staticmethod
    def diffDates(*manydates, type="days"):
        my_dates = sorted(manydates)        
        return rdelta.relativedelta(my_dates[len(my_dates)-1], my_dates[0]).__getattribute__(type)
    
        
        
if __name__ == "__main__":
    #fechas = [datetime.date(2022, 1, 1), datetime.date(1980, 1, 2), datetime.date(2019, 1, 3), datetime.date(1999, 10, 11)]
    #fechas = [date.datetime(1969, 1, 15), date.datetime(2023, 11, 13), date.datetime(2023, 11, 15), date.today()]
    #print(GestFechas.getOldDate(*fechas))

    #print(GestFechas.diffDates(*fechas, type="years"))
    from datetime import datetime
    from datetime import timedelta

    #Sumar dos días a la fecha actual
    now = datetime.date(1999, 1, 1)
    new_date = now + timedelta(days=2)
    print(new_date)

    #Comparación
    if now < new_date:
        print("La fecha actual es menor que la nueva fecha")