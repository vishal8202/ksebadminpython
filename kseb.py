import mysql.connector
from datetime import date
from tabulate import tabulate
import random
try:
        mydb = mysql.connector.connect(host = 'localhost',user = 'root' ,password = '',database = 'ksebdb')
except mysql.connector.Error as e:
        print("MySql error",e)
mycursor = mydb.cursor()
while True:
    print("select an option from the menu")
    print("""           1. add consumer
             2. search consumer
             3. delete  consumer
             4. update the consumer
             5. view all consumer
             6. generate bill
             7. view bill
             8. view top 2 bill 
             9.Exit """)
    choice =int(input("Enter your option : "))
    if (choice==1):
        print("add consumer selected")
        consumer_id = int(input("Enter the consumer id: "))
        name = input("enter the name :")
        phone = input("Enter the phone number : ")
        place = input("Enter the address : ")
        email = input("Enter the email id : ")
        sql = "INSERT INTO `consumer`(`id`, `consumer_code`, `consumer_name`, `consumer_phone`, `consumer_email`, `consumer_adress`) VALUES (%s,%s,%s,%s,%s)"
        data =(consumer_id,name,phone,place,email)
        mycursor.execute(sql,data)
        mydb.commit()
    elif(choice==2):
        print("search consumer selected")
        search = input("enter the consumer code, consumer name ,phone number : ")
        sql = "SELECT `id`, `consumer_code`, `consumer_name`, `consumer_phone`, `consumer_email`, `consumer_adress` FROM `consumer` WHERE `consumer_code`= '"+search+"' OR `consumer_name`='"+search+"' OR `consumer_phone`= '"+search+"'"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        for i in result:
            print(i) 
    elif(choice == 3):
        print("Delete Consumer Selected")
        consumer_code = input("Enter the consumer code to delete: ")
        sql = "DELETE FROM `consumer` WHERE `consumer_code`="+consumer_code
        mycursor.execute(sql)
        mydb.commit()
        print("Data deleted successfully.")
    elif(choice == 4):
        print("Update Consumer selected")
        consumer_code = input("Enter the consumer code to update consumer: ")
        consumer_name = input("Enter the consumer name to update: ")
        consumer_phone = input("Enter the consumer phone to update: ")
        consumer_email = input("Enter the consumer email id to update: ")
        consumer_address = input("Enter the consumer address to update: ")
        sql = "UPDATE `consumer` SET `consumer_name`='"+consumer_name+"',`consumer_phone`='"+consumer_phone+"',`consumer_email`='"+consumer_email+"',`consumer_address`='"+consumer_address+"' WHERE `consumerCode` = "+consumer_code
        mycursor.execute(sql)
        mydb.commit()
        print("Data updated successfully")
    
    elif(choice == 5):
        print("View All Consumer selected")
        sql = "SELECT `consumer_code`, `consumer_name`, `consumer_phone`, `consumer_email`, `consumer_adress` FROM `consumer`   "
        mycursor.execute(sql)
        result = mycursor.fetchall()
        for i in result:
            print(i)
    elif(choice==6):
        print("You had entered into generate bill section ")
        dates = date.today()
        year = dates.year
        month = dates.month
        sql = "DELETE FROM `bill` WHERE `month`='"+str(month)+"' AND `year`='"+str(year)+"'"
        print(sql)
        mycursor.execute(sql)
        mydb.commit()
        sql = "SELECT `id` FROM `consumer` "
        mycursor.execute(sql)
        result = mycursor.fetchall()
        for i in result:
            print(i[0])
            id = i[0]
            sql = "SELECT SUM(`unit`) FROM `usages` WHERE `consumer_code`='"+str(i[0])+"'  AND MONTH(`datetime`)='"+str(month)+"' AND YEAR(`datetime`)='"+str(year)+"'"
            mycursor.execute(sql)
            result = mycursor.fetchone()
            unit = result[0]
            print(unit)
            total_bill = int(str(result[0])) * 5
            print(total_bill)
            status = 0
            invoice = random.randint(10000,100000)
            sql = "INSERT INTO `bill`(`consumer_code`, `month`, `year`, `bill`, `paid_status`, `bill_date`,`total_units`,`duedate`, `invoice`) VALUES (%s,%s,%s,%s,%s,now(),%s,now()+interval 14 day,%s)"
            data = (str(id),str(month),str(year),total_bill,status,str(unit),str(invoice))
            mycursor.execute(sql , data)
            mydb.commit()
       
    elif(choice == 7):
        print("view the bill which had generated ")
        sql = "SELECT  c.consumer_name,c.consumer_adress,b.`month`, b.`year`, b.`bill`, b.`paid_status`, b.`bill_date`, b.`total_units`, b.`duedate`, b.`invoice` FROM `bill` b JOIN consumer c ON b.consumer_code=c.id"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        print(tabulate(result,headers=['consumer_name','consumer_adress','month','year','bill','paid_status','bill_date','total_units','duedate','invoice'],tablefmt = "psql"))
    elif(choice==8):
        print('Top 2 high bill')
        sql = "SELECT c.consumer_name,c.consumer_adress,b.`bill`, b.`total_units` FROM `bill` b JOIN consumer c ON b.consumer_code=c.id ORDER BY b.`bill`DESC LIMIT 2"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        print(tabulate(result,headers=['consumer_name','consumer_adress','bill', 'total_units']))

    
    elif choice==9:
        break

