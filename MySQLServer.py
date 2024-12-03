import mysql.connector

def create_database(host, user, password):
  """
  Creates the database 'alx_book_store' if it doesn't exist.

  Args:
      host: The hostname of the MySQL server.
      user: The username for accessing the MySQL server.
      password: The password for the user.
  """
  try:
    mydb = mysql.connector.connect(
        host=host,
        user=user,
        password=password
    )

    mycursor = mydb.cursor()

    # Create the database (ignoring existing database errors)
    mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

    print("Database 'alx_book_store' created successfully!")

  except mysql.connector.Error as err:
    print("Error creating database:", err)
  finally:
    if mydb:
      mycursor.close()
      mydb.close()

if __name__ == "__main__":
  # Replace with your actual MySQL credentials
  host = "your_host"
  user = "your_user"
  password = "your_password"

  create_database(host, user, password)