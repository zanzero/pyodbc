from cnxn import cursor,cnxn

name = "Sansa"
age = "46"
city = "MYL"

cursor.execute("INSERT INTO dbo.pyodbctable(Name, Age, City) VALUES (?, ?, ?)", name, age, city)
cnxn.commit()