from errno import errorcode
import mysql.connector

# Verbindungsinformationen
host = "127.0.0.1"
user = "userdb"
password = "userdb"
database = "inventory"

# Verbindung herstellen
try:
    conn = mysql.connector.connect(host=host,user=user,password=password)
    print("Connection established")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with the user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    cursor = conn.cursor()




def sqlQuery(colour, Quantity):

    Query = '''SELECT PI.Quantity_Current, PT.Shelf_ID, PT.QRCode 
        FROM inventory.tfact_packageinventory as PI
        INNER JOIN inventory.tdim_packagetype as PT
        ON     PI.PackageType_ID = PT.PackageType_ID
        WHERE  PT.Colour = "%s"''' %colour


    cursor.execute(Query)

    for row in cursor:
        available_quantity = row[0]
        position_Shelf = row[1]
        QR_Code = row[2]

        if(Quantity<=available_quantity):
            print("verfügbare Menge: " + str(available_quantity)) 
            print("Position: " + str(position_Shelf))
            print("QR-Code: " + str(QR_Code))
        else:
            position_Shelf = -1
            print("Not enough packages of %s colour available" %colour)

    return position_Shelf, available_quantity

def sqlAdd():
    colour_need = input("Vefügbare Farbe: ")
    
    Query = 'SELECT PackageType_ID FROM inventory.tdim_packageType WHERE Colour = "%s"' %colour_need
    cursor.execute(Query)

    for row in cursor:
        packageType_ID = row[0]
        print(str(packageType_ID))

    Query_insert = '''INSERT INTO inventory.tfact_packagemovement(PackageType_ID, Quantity)
        VALUES('%d', '1')''' %packageType_ID
    
    cursor.execute(Query_insert)
    conn.commit()
    print("Package has added!")

    Query_Quantity = '''UPDATE inventory.tfact_packageinventory 
        SET Quantity_Current = (Quantity_Current + 1) WHERE PackageType_ID = "%d" ''' %packageType_ID
    
    cursor.execute(Query_Quantity)
    conn.commit()


def sqlRemove():
    colour_need = input("Benötigte Farbe: ")

    Query = 'SELECT PackageType_ID FROM inventory.tdim_packageType WHERE Colour = "%s"' %colour_need
    cursor.execute(Query)

    for row in cursor:
        packageType_ID = row[0]
        

    Query_remove = '''INSERT INTO inventory.tfact_packagemovement(PackageType_ID, Quantity)
        VALUES('%d', '-1')''' %packageType_ID
    
    cursor.execute(Query_remove)
    conn.commit()
    print("Package has been removed!")

    Query_Quantity = '''UPDATE inventory.tfact_packageinventory 
        SET Quantity_Current = (Quantity_Current - 1) WHERE PackageType_ID = "%d" ''' %packageType_ID
    
    cursor.execute(Query_Quantity)
    conn.commit()



while True:
    x = int(input("Wählen Sie eine Möglichkeit!\nPaket auslesen(1)\nPaket hinzufügen(2)\nPaket entfernen(3)\n"))
    
    if(x == 1):
        colour = input("\nBenötigte Farbe: ")
        Quantity = int(input("\nMenge: "))
        sqlQuery(colour, Quantity)
    elif(x == 2):
        sqlAdd()     
    elif(x == 3):
        sqlRemove()
    else:
        print("Falsche Zahl eingegeben!\n\n")
        cursor.close()
        conn.close()
        break    
    



 




