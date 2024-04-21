import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "student_management"
)
#creating database
mycursor = mydb.cursor()
'''mycursor.execute("create database student_management")
print("Database created successfully.")'''

#creating table
'''mycursor.execute("create table students(Student_ID int Primary Key Auto_Increment, Name varchar(155), Age int(2), Gender varchar(6), DOB varchar(15), Address varchar(122), Contact varchar(10), Attendence varchar(20))")
print("Table created successfully.")'''

#inserting data
sql = "insert into students(Student_ID,Name,Age,Gender,DOB,Address,Contact,Attendence) values(%s,%s,%s,%s,%s,%s,%s,%s)"
val = [
    ('', "Bob", "16" , "Male", "12-12-2007","Delhi","8523467950","85%"),
    ('', "Finlo", "15" , "Female", "05-04-2008","Mumbai","8754236197","65%"),
    ('', "Arlo", "18" , "Male", "08-07-2005","Goa","7512345680","55%"),
    ('', "Zena", "15" , "Female", "16-08-2008","Mumbai","7577701950","72%"),
    ('', "Luci", "17" , "Female", "10-06-2006","Punjab","9575856555","40%"),
    ('', "Anura", "15" , "Female", "22-09-2008","Gujrat","8519734652","40%"),
    ('', "Reva", "16" , "Male", "26-01-2007","kerela","9171569420","68%"),
    ('', "Vanca", "17" , "Female", "16-09-2006","Sikkim","8696465060","78%"),
    ('', "Ahaan", "14" , "Male", "28-07-2009","Delhi","9570428100","92%"),
    ('', "Evan", "19" , "Male", "19-04-2004","Chennai","9868183780","33%"),
    ('', "Gaur", "17" , "Male", "30-01-2006","Darjeeling","8511501780","90%"),
    ('', "Ivaan", "19" , "Male", "19-03-2004","Chennai","8378054976","59%")
]
mycursor.executemany(sql,val)
mydb.commit()
print("Data inserted successfully.")