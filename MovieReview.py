import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="*****",
    database="movie_db"
)

cursor = db.cursor()

def add_movie(title, director, year, rating):
    sql = "INSERT INTO movies (title, director, release_year, rating) VALUES (%s, %s, %s, %s)"
    values = (title, director, year, rating)
    cursor.execute(sql, values)
    db.commit()
    print("Movie added!")

def view_movies():
    cursor.execute("SELECT * FROM movies")
    for row in cursor.fetchall():
        print(row)

def update_rating(movie_id, new_rating):
    sql = "UPDATE movies SET rating = %s WHERE movie_id = %s"
    cursor.execute(sql, (new_rating, movie_id))
    db.commit()
    print("Movie updated!")

def delete_movie(movie_id):
    sql = "DELETE FROM movies WHERE movie_id = %s"
    cursor.execute(sql, (movie_id,))
    db.commit()
    print("Movie deleted!")


while True:
    print("\nMovie Database")
    print("1. View Movies")
    print("2. Add Movie")
    print("3. Update Rating")
    print("4. Delete Movie")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        view_movies()

    elif choice == "2":
        title = input("Title: ")
        director = input("Director: ")
        year = int(input("Release Year: "))
        rating = float(input("Rating: "))
        add_movie(title, director, year, rating)

    elif choice == "3":
        movie_id = int(input("Movie ID: "))
        rating = float(input("New Rating: "))
        update_rating(movie_id, rating)

    elif choice == "4":
        movie_id = int(input("Movie ID: "))
        delete_movie(movie_id)

    elif choice == "5":
        break

    else:
        print("Invalid choice.")
