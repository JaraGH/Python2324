# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from  mysql_module import Mysql

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm testing MySql')

    con = Mysql(host='127.0.0.1', port=3306, user='root', password='10negritos10@@', database='classicmodels')

    print(con.connect().is_connected())
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
