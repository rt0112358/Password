from cryptography.fernet import Fernet
import mysql.connector
from mysql.connector import Error
import password
import sign_in

key = Fernet.generate_key() # key to encrypt and decrypt
print("Enter the password you would like to use: ")
pword = password.get_password() # User entered password
password = pword.encode() # passsword for something

go = Fernet(key) # object to encrypt and decrypt

# the key is needed to encrypt and decrypt
encrypted = go.encrypt(password)
decrypted = go.decrypt(encrypted)

# Output stats
print("Your key: " + str(key))
print("Password: " + str(password))
print("Encrypted password: " + str(encrypted))
print("decrypted password: " + str(decrypted))


encrypted = str(encrypted)
print(type(encrypted))

encrypted = encrypted.strip("'b'=")
print(encrypted)

def get_password():
    ret_val = password
    return ret_val

# get_password(encrypte)

host_name = sign_in.host_name()
database_name = sign_in.database()
username = sign_in.username()
pword = sign_in.pword()


try:
    connection = mysql.connector.connect(host=host_name,
                                         database=database_name,
                                         user=username,
                                         password=pword)
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: " + str(record))

        sql_select_Query = "select * from users;"
        cursor = connection.cursor()
        
        cursor.execute(sql_select_Query)

        data = cursor.fetchall()
        
        username = "Qwerty"


        insert_query = "insert into users values(42,'" + str(username) + "','" + str(encrypted) + "')"
        # print(insert_query)
        cursor.execute(insert_query)
        connection.commit()
        cursor.execute(sql_select_Query)
        data = cursor.fetchall()
        connection.commit()

        print("\n\ndata from users tables:")
        for row in data:
            print(row)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")


# TODO: Clean up
# TODO: Use key to access encrypted passwords in database
