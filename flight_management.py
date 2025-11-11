import csv 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



def menu():
    print('''            ****************************************************************************) 
                                      FLIGHT MANGEMENT PROJECT")
            ****************************************************************************)
                                    1.Read Flight Records
                                    2.Employee Information
                                    3.Passenger Information
                                    4.Enter New Flight Record
                                    5.Total Flights
                                    6.Reading Records
                                    7.Add Passenger Information
                                    8.Display special column of Passenger
                                    9.Display special column of Flight
                                   10.Display special column of Employee
                                   11.Updatin Flight Flie
                                   12.Sorting Destination Names
                                   13.Enter New Employee Record
                                   14.Information About max. & Min. Salaries
                                   15.Line graph of Employee and Their Salaries
                                   16.Horizontal Bar Graph of Employee and Their Salaries
                                   17.Bar Graph of Employee and Their Salaries
                                   18.Line graph of  Passengers and Their Fare
                                   19.Horizontal Bar Graph of Passengers and Their Fare
                                   20.Bar Graph of Passengers and Their Fare
 
            *****************************************************************************''')


def read_record():
    print("Read Flight Records")
    cv=pd.read_csv(("flight.csv"),index_col=0)
    print(cv)

def employee_record():
    print("Employee Information")
    cv=pd.read_csv("Flight emp.csv",index_col=0)
    print(cv)

def passenger_record():
    print("Passenger Information")
    cv=pd.read_csv("passanger.csv",index_col=0)
    print(cv)

def add_flight():
    print("Enter New Record in File Flight")
    df=pd.read_csv("Flight emp.csv")
    SN=int(input("Enter Serial No: "))
    F=int(input("Enter Flight No: "))
    N=input("Enter Flight Name: ")
    S=input("Enter Flight Source: ")
    D=input("Enter Destination: ")
    NA=input("Enter Number of stops: ")
    FA=int(input("Enter Fare: "))
    FR=int(input("Enter Frequency: "))
    DD=str(input("Enter Date of Departure: "))
    df=df.append({'S_No.':SN,'F_No.':F,'F_Name':N,'Source':S,'Destination':D,r'Non stop \ upto 1 stop\ upto 2 stop':NA,'Fare':FA,'Frequency':FR,'Date of Departure':DD},ignore_index=True)
    print(df)
    print("Recorded Added")

def Total_flight():
    print("Total Flights")
    df=pd.read_csv("flight.csv")
    Totalflights=df['F_Name'].count()
    print(Totalflights)

def read_fewrows():
    print("Read Few Rows")
    df=pd.read_csv("flight.csv",nrows=2)
    print("Show 2 Records")
    print(df)
    
def add_pess():
    print("Enter New Pessanger Record")
    df=pd.read_csv("passanger.csv")
    P=int(input("Enter Pessanger ID: "))
    N=input("Enter pessanger Name: ")
    F=int(input("Enter Flight No: "))
    FA=int(input("Enter Fare Charges: "))
    S=input("Enter Source: ")
    D=input("Enter Destination: ")
    M=int(input("Enter Mobile No: "))
    A=input("Enter Address: ")
    df= df.append({'Pid':P,'Pname':N,'Fno':F,'Fare':FA,'Source':S,'Destination':D,'Mobile':M,'Address':A},ignore_index=True)
    print(df)
    print("Record Added")

def spec_col_pass():
    print("Display specific passenger Columns")
    df=pd.read_csv("passanger.csv",usecols=['Pname'])
    print(df)

def spec_col_flight():
    print("Display specific flight Columns")
    df=pd.read_csv("flight.csv",usecols=['F_No.'])
    print(df)

def spec_col_emp():
    print("Display specific employee Columns")
    df=pd.read_csv("Flight emp.csv",usecols=['Ename'])
    print(df)

def update_flight():
    print("To increase Fare and save")
    print("Previous Fare")
    print()
    df=pd.read_csv("flight.csv")
    print(df)
    print()
    print("Increase Fare by 1000")
    print()
    df=pd.read_csv("flight.csv")
    df['Fare']+=1000
    print(df)

def sort_desc():
    print("Display Destination in Descending Order")
    print()
    df=pd.read_csv("flight.csv",index_col=0)
    df=df.sort_values('Destination',ascending=False)
    print(df)

def new_emp():
    print("Enter Details of New Emp")
    df=pd.read_csv("Flight emp.csv")
    E=int(input("Enter Emp No: "))
    N=input("Enter Emp Name: ")
    D=input("Enter DOJ: ")
    M=int(input("Enter Mobile No: "))
    D=input("Enter Designation: ")
    S=int(input("Enter Salary: "))
    df=df.append({'Eno':E,'Ename':N,'DOJ':D,'Mobile':M,'Designation':D,'Salary':S},ignore_index=True)
    print(df)
    print("Record Added")
    
def maxminsal():
    print("Maximum and minimum salary of Emp")
    df=pd.read_csv("Flight emp.csv")
    print(df)
    print()
    print("Highest Salary")
    print(df.Salary.max())
    print()
    print("lowest salary")
    print(df.Salary.min())

def Line_plot():
    print("Line Plot")
    df=pd.read_csv("Flight emp.csv")
    print(df)
    x=df['Ename']
    y=df['Salary']
    plt.xlabel("Flight Emp")
    plt.ylabel("Salary")
    plt.xticks(rotation=30)
    plt.title("Employee record")
    plt.grid(True)
    plt.plot(x,y,marker='x',linewidth=10,color='r')
    plt.show()

def Horbar_plot():
    print("Bar Plot")
    df=pd.read_csv("Flight emp.csv")
    print(df)
    x=df['Ename']
    y=df['Salary']
    plt.title('Flight employee and their Salaries')
    plt.xlabel('Salary')
    plt.ylabel('Ename')
    plt.barh(x,y,color='y')
    plt.show()

def Bar_plot():
    print("Bar Plot")
    df=pd.read_csv("Flight emp.csv")
    print(df)
    x=df['Ename']
    y=df['Salary']
    plt.title('Flight Employee and their Salaries')
    plt.xlabel('Ename')
    plt.ylabel('Salary')
    plt.bar(x,y,color=['gold','green'])
    plt.show()
    
def Line_plot_pass():
    print("Line Plot")
    df=pd.read_csv("passanger.csv")
    print(df)
    x=df['Pname']
    y=df['Fare']
    plt.xlabel("Passenger")
    plt.ylabel("Fare")
    plt.xticks(rotation=30)
    plt.title("Passenger")
    plt.grid(True)
    plt.plot(x,y,marker='x',linewidth=10,color='c')
    plt.show()

def Horbar_plot_pass():
    print("Bar Plot")
    df=pd.read_csv("passanger.csv")
    print(df)
    x=df['Pname']
    y=df['Fare']
    plt.title('Passenger and their Fare')
    plt.xlabel('Fare')
    plt.ylabel('Passenger')
    plt.barh(x,y,color='r')
    plt.show()

def Bar_plot_pass():
    print("Bar Plot")
    df=pd.read_csv("passanger.csv")
    print(df)
    x=df['Pname']
    y=df['Fare']
    plt.title('Passenger and their Fare')
    plt.xlabel('Pname')
    plt.ylabel('Fare')
    plt.bar(x,y,color=['m','b'])
    plt.show()
    

while True:
    menu()  # Show menu every time
    try:
        opt = int(input("Enter Your Choice: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if opt == 1:
        read_record()
    elif opt == 2:
        employee_record()
    elif opt == 3:
        passenger_record()
    elif opt == 4:
        add_flight()
    elif opt == 5:
        Total_flight()
    elif opt == 6:
        read_fewrows()
    elif opt == 7:
        add_pess()
    elif opt == 8:
        spec_col_pass()
    elif opt == 9:
        spec_col_flight()
    elif opt == 10:
        spec_col_emp()
    elif opt == 11:
        update_flight()
    elif opt == 12:
        sort_desc()
    elif opt == 13:
        new_emp()
    elif opt == 14:
        maxminsal()
    elif opt == 15:
        Line_plot()
    elif opt == 16:
        Horbar_plot()
    elif opt == 17:
        Bar_plot()
    elif opt == 18:
        Line_plot_pass()
    elif opt == 19:
        Horbar_plot_pass()
    elif opt == 20:
        Bar_plot_pass()
    elif opt == 0:
        print("Exiting program. Goodbye!")
        break
    else:
        print("INVALID OPTION")


