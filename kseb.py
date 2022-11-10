import mysql.connector

mydb = mysql.connector.connect(host = 'localhost' , user = 'root' , password = '' , database = 'ksebdb')

mycursor = mydb.cursor()

mycursor = mydb.cursor()
while True:
    print("select an option from the menu")
    print('1 add consumer')
    print('2 search consumer')
    print('3 delete consumer')
    print('4 update consumer')
    print('5 view all  consumer')
    print('6 generate bill consumer')
    print('7 view bill')
    print('8 exit')

       choice = int(input('Enter an option: '))
       if(choice==1):
        print('enter consumer details')
        elif(choice==2):
            print('search consumer')   
         elif(choice==3):
            print('delete consumer')  
         elif(choice==4):
            print('update consumer') 
         elif(choice==5):
            print('view all consumer')  
         elif(choice==6):
            print('generate bill ') 
         elif(choice==7):
            print('view bill')   
         elif(choice==8):
         break

        