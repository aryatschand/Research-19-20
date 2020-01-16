#!/usr/bin/python3
import pymysql
import random

def insertPoint(plant_num, empirical, theoretical, color, heat, light, healthy):
   water = round(min([theoretical, empirical]) * 0.67 + max([theoretical, empirical]) * 0.33,2)
   # Open database connection
   db = pymysql.connect("localhost","root","parWONE123","plant_data_1920" )

   # prepare a cursor object using cursor() method
   cursor = db.cursor()

   # Prepare SQL query to INSERT a record into the database.
   sql = "INSERT INTO `irrigation_data` (`id`, `plant_num`, `water`,`color`,`temperature`, `photoresistance`) VALUES (NULL, '{}', '{}', '{}', '{}', '{}');" .format(plant_num, water, color, heat, light)
   try:
   # Execute the SQL command
      cursor.execute(sql)
   # Commit your changes in the database
      db.commit()
   except:
   # Rollback in case there is any error
      db.rollback()
   # disconnect from server
   sql = ""
   if healthy == True:
      sql = "INSERT INTO `micropiece_commands` (`id`, `plant_num`, `water_volume`,`empirical`,`theoretical`, `notes`) VALUES (NULL, '{}', '{}', '{}', '{}', '{}');" .format(plant_num, water, round(empirical, 2), round(theoretical, 2), 'healthy')
   else:
      sql = "INSERT INTO `micropiece_commands` (`id`, `plant_num`, `water_volume`,`empirical`,`theoretical`, `notes`) VALUES (NULL, '{}', '{}', '{}', '{}', '{}');" .format(plant_num, water, round(empirical, 2), round(theoretical, 2), 'unhealthy')
   try:
   # Execute the SQL command
      cursor.execute(sql)
   # Commit your changes in the database
      db.commit()
   except:
   # Rollback in case there is any error
      print("error into micropiece")
      db.rollback()
   db.close()
