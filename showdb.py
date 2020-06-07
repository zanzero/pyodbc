from cnxn import cursor,cnxn

cursor.execute('SELECT Age,Name,City FROM pyodbc.dbo.pyodbctable')

i = 1
for row in cursor.fetchall():
    print(i)
    print("Name : ",row.Name)
    print("Age : ",row.Age)
    print("City : ",row.City)
    print("***************")
    i = i+1
