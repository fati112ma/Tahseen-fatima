import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "recipe_management"
)
#creating database
mycursor = mydb.cursor()
'''mycursor.execute("create database recipe_management")
print("Database created successfully.")'''

#creating table
'''mycursor.execute("create table recipe(Recipe_ID int Primary Key Auto_Increment, title varchar(100), desciption varchar(100), ingredients varchar(100), preparation_time varchar(15), cooking_time varchar(15), total_time varchar(10), difficulty_level varchar(20), cuisine varchar(30), calories varchar(30))")
print("Table created successfully.")'''

#inserting data
sql = "insert into recipe(Recipe_ID,title,desciption,ingredients,preparation_time,cooking_time,total_time,difficulty_level,cuisine,calories) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
val = [
    ('', "Spaghetti Carbonara", "A classic Italian pasta dish" , "Spaghetti, eggs, pancetta or bacon, Parmesan cheese, black pepper", "10 minutes","10 minutes","20 minutes","Easy","Italian","450 cal per serving"),
    ('', "Chicken Tikka Masala", "A popular Indian dish consisting of marinated and grilled chicken pieces","Chicken breasts, yogurt, lemon juice, garlic, ginger, garam masala, cumin, paprika, tomatoes, cream, butter","30 minutes","30 minutes","1 hour","Medium","Indian","400 cal per serving"),
    ('', "Sushi Rolls", "Japanese rice rolls filled with various ingredients" , "Sushi rice, nori (seaweed), raw fish (e.g., salmon, tuna), cucumber, avocado, carrots, soy sauce, wasabi", "30 minutes","0 minutes","30 minutes","Diffcult","Japanese","200 cal per roll"),
    ('', "Vegetable Curry", "A flavorful Indian dish made with a variety of vegetables" , "Assorted vegetables (potatoes, carrots, peas, cauliflower, bell peppers), onions, garlic, ginger, tomatoes, spices ", "20 minutes","30 minutes","50 minutes","Medium","Indian","250 cal per serving"),
    ('', "Chole Bhature", "A popular North Indian street food dish consisting of spicy chickpea curry" , "Chickpeas, onions, tomatoes, ginger, garlic, green chilies, spices (coriander, cumin, garam masala), lemon juice, cilantro, flour, baking powder, oil, salt", "20 minutes","40 minutes","1 hour","Medium","Indian","500 cal per serving"),
    ('', "Vegetable Pulao", "A fragrant and flavorful Indian rice dish" , "Basmati rice, mixed vegetables (carrots, peas, beans), onions, tomatoes, ginger-garlic paste, spices (cumin seeds, cinnamon, cloves, cardamom), ghee, salt", "15 minutes","20 minutes","35 minutes","Easy","Indian","250 cal per serving"),
    ('', "Palak Paneer", "A popular North Indian dish made with fresh spinach" , "Spinach, paneer, tomatoes, onions, garlic, ginger, green chilies, cream, garam masala, turmeric, cumin seeds, salt, oil", "15 minutes","20 minutes","35 minutes","Medium","Indian","300 cal per serving"),
]
mycursor.executemany(sql,val)
mydb.commit()
print("Data inserted successfully.")