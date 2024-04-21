import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "inventory_management"
)

#creating database 
mycursor = mydb.cursor()
'''mycursor.execute("create database inventory_management")
print("Database created successfully")'''

#creating table
'''mycursor.execute("create table inventory(Item_ID int Primary Key Auto_Increment, item_name varchar(50), category varchar(50), brand varchar(50), quantity varchar(15), unit_price char(15), total_price varchar(100))")
print("Table created successfully.")'''

#inserting data
sql = "insert into inventory(Item_ID,item_name,category,brand,quantity,unit,total_price) values(%s,%s,%s,%s,%s,%s,%s)"
val = [
    ('',"Laptop","Electronics","Dell","10","$800","$8000"),
    ('',"Rice","Groceries","ABC Rice Company","100","$10","$000"),
    ('',"Smartphone","Electronics","Samsung","15","$700","$10500"),
    ('',"Backpack","Accessories","North Face","5","$20","$200"),
    ('',"Desk Lamp","Home Accessories","Ikea","3","$5","$25")
]
mycursor.executemany(sql,val)
mydb.commit()
print("Data inserted successfully.")