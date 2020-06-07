import pyodbc 
cnxn = pyodbc.connect('Driver={SQL Server};'
                      'Server=10.100.5.216;'
                      'Database=CISCODB;'
                      'UID=sa;'
                      'PWD=###Password')
                      
cursor = cnxn.cursor()