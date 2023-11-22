from datetime import date
import dateutil.relativedelta  as rdelta

class GestFechas:
    @staticmethod
    def getOldDate(*manydates):
        my_dates = sorted(manydates)
        return my_dates[0]
    
    @staticmethod
    def diffDates(date1, date2):
        if date1>date2:
            date1, date2 = date2, date1
        diff = date2-date1
        return diff.days
        
    @staticmethod
    def sortDates(*manydates, orden='ASC'):
        return sorted(manydates, reverse=True) if orden=='DESC' else sorted(manydates)
        
        
if __name__ == "__main__":
    fechas = [date(2022, 1, 1), date(1980, 1, 2), date(2019, 1, 3), date(1999, 10, 11)]
    
    mi_nacimiento = date(1969, 1, 15)
    print(GestFechas.diffDates(date.today(), mi_nacimiento))




    
    
    
    

    