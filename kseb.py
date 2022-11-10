
import mysql.connector
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
             5. view all consmer
             6. generate bill
             7. view bill
             8. Exit """)
    choice =int(input("Enter your option : "))
    if choice==1:
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
        consumer_eddress = input("Enter the consumer address to update: ")
        sql = "UPDATE `consumer` SET `consumer_name`='"+consumename+"',`consumer_phone`='"+consumerphone+"',`consumer_email`='"+consumeremail+"',`consumer_address`='"+consumeraddress+"' WHERE `consumerCode` = "+consumercode
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
    elif(choice == 6):
        print("Generate Bill selected")
    elif(choice == 7):
        print("View Bill selected")
    elif choice==8:
        break