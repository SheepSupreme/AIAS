import mysql.connector
from errno import errorcode
from datetime import datetime, timedelta
from tkinter import messagebox


host = "127.0.0.1"
user = "userdb"
password = "userdb"
database = "aks" 

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


def add_package_to_issue(ID):

    query = "SELECT issue_datetime FROM aks.tdim_inventory WHERE ID = %s" %ID
    cursor.execute(query)
    issue_datetime = cursor.fetchall()[0][0]
                    
    query_y = "SELECT MAX(position_y) FROM aks.tfact_issue_inventory WHERE position_x = 1"
    cursor.execute(query_y)
    result = cursor.fetchall()

    if result and result[0][0] is not None:
        max_y = int(result[0][0])

        query = '''SELECT issue_datetime FROM aks.tfact_issue_inventory WHERE position_x = 1 
                AND position_y = %s''' %max_y
        cursor.execute(query)
        result = cursor.fetchall()

    
        for row in result:
            issue_datetime_old = row[0]
            print(issue_datetime_old)
            issue_datetime_old_seconds = (issue_datetime_old - datetime.now()).total_seconds()
            
            issue_datetime_new_seconds = (issue_datetime - datetime.now()).total_seconds()

            if issue_datetime_new_seconds >= issue_datetime_old_seconds and max_y < 3:
                max_y = max_y + 1
                query_insert = '''INSERT INTO aks.tfact_issue_inventory(ID, issue_datetime, position_x, position_y)
                                VALUES(%s, %s, 1, %s)''' 
                cursor.execute(query_insert, (ID, issue_datetime, max_y))
                conn.commit()
                print("Package has been added!")
            else:
                query_y = "SELECT MAX(position_y) FROM aks.tfact_issue_inventory WHERE position_x = 2"
                cursor.execute(query_y)
                result = cursor.fetchall()
                
                print("test")

                if result and result[0][0] is not None:
                    max_y = int(result[0][0])

                    print("test1")

                    query = '''SELECT issue_datetime FROM aks.tfact_issue_inventory WHERE position_x = 2 
                            AND position_y = %s''' %max_y
                    cursor.execute(query)
                    result = cursor.fetchall()

                
                    for row in result:
                        issue_datetime_old = row[0]
                        issue_datetime_old_seconds = (issue_datetime_old - datetime.now()).total_seconds()
                        
                        issue_datetime_new_seconds = (issue_datetime - datetime.now()).total_seconds()

                        if issue_datetime_new_seconds >= issue_datetime_old_seconds and max_y < 3:
                            max_y = max_y + 1
                            query_insert = '''INSERT INTO aks.tfact_issue_inventory(ID, issue_datetime, position_x, position_y)
                                            VALUES(%s, %s, 2, %s)'''
                            cursor.execute(query_insert, (ID, issue_datetime, max_y))
                            conn.commit()
                            print("Package has been added")
                        else:
                            query_y = "SELECT MAX(position_y) FROM aks.tfact_issue_inventory WHERE position_x = 3"
                            cursor.execute(query_y)
                            result = cursor.fetchall()

                            if result and result[0][0] is not None:
                                max_y = int(result[0][0])

                                query = '''SELECT issue_datetime FROM aks.tfact_issue_inventory WHERE position_x = 3 
                                        AND position_y = %s''' %max_y
                                cursor.execute(query)
                                result = cursor.fetchall()

                            
                                for row in result:
                                    issue_datetime_old = row[0]
                                    issue_datetime_old_seconds = (issue_datetime_old - datetime.now()).total_seconds()
                                    
                                    issue_datetime_new_seconds = (issue_datetime - datetime.now()).total_seconds()

                                    if issue_datetime_new_seconds >= issue_datetime_old_seconds and max_y < 3:
                                        max_y = max_y + 1
                                        query_insert = '''INSERT INTO aks.tfact_issue_inventory(ID, issue_datetime, position_x, position_y)
                                                        VALUES(%s, %s, 3, %s)'''
                                        cursor.execute(query_insert, (ID, issue_datetime, max_y))
                                        conn.commit()
                                        print("Package has been added")
                                    else:
                                        messagebox.showwarning(title=None, message="Package can not be placed into the Issue Storage!")
                            else:
                                query_insert = '''INSERT INTO aks.tfact_issue_inventory(ID, issue_datetime, position_x, position_y)
                                            VALUES(%s, %s, 3, 1)'''
                                cursor.execute(query_insert, (ID, issue_datetime))
                                conn.commit()
                                print("Package has been added")
                else:
                    print("test2")
                    query_insert = '''INSERT INTO aks.tfact_issue_inventory(ID, issue_datetime, position_x, position_y)
                            VALUES(%s, %s, 2, 1)'''
                    cursor.execute(query_insert, (ID, issue_datetime))
                    conn.commit()
                    print("Package has been added")

    else: 
        query_insert = '''INSERT INTO aks.tfact_issue_inventory(ID, issue_datetime, position_x, position_y)
                        VALUES(%s, %s, 1, 1)'''
        cursor.execute(query_insert, (ID, issue_datetime))
        conn.commit()