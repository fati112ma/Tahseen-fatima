import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "Library_Books_Management"
)
#creating database 
mycursor = mydb.cursor()
'''mycursor.execute("create database Library_Books_Management")
print("Database created successfully")'''

#creating table
'''mycursor.execute("create table books(Book_ID int Primary Key Auto_Increment, Title varchar(100), Author varchar(50), Publisher varchar(50), Publication_Year varchar(15), Language char(15), Number_of_Pages varchar(150), Book_Condition varchar(10), Availability varchar(10))")
print("Table created successfully.")'''

#inserting data
sql = "insert into books(Book_ID,Title,Author,Publisher,Publication_Date,Language,Number_of_Pages,Availability,Book_Condition) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
val = [
    ('',"Pride and Prejudice","Jane Austen","Thomas Egerton","1813","English","400","New","Yes"),   
    ('',"The Lord of the Rings"," J.R.R. Tolkien","George Allen & Unwin","1954","English","1,500","Old","New"),
    ('',"Computer Networking: A Top-Down Approac","James F. Kurose, Keith W. Ross","Pearson","2016","English","864","New","Yes"),
    ('',"Artificial Intelligence: A Modern Approach","Stuart Russell, Peter Norvig","Pearson","2015","English","1152","New","No"),
    ('',"One Hundred Years of Solitude","Gabriel García Márquez","Editorial Sudamericana","1967","English","500","Yes","New"),
    ('',"Der Steppenwolf","Hermann Hesse"," S. Fischer Verlag","1927","German","400","No","Old"),
    ('',"Clean Code: A Handbook of Agile Software Craftsmanship","obert C. Martin","Prentice Hall","2008","English","464","No","New")
]
mycursor.executemany(sql,val)
mydb.commit()
print("Data inserted successfully.")