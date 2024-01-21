import sqlite3
import csv

conn = sqlite3.connect(r'D:\Personal Projects\Website\GamersEdgeStore\db.sqlite3')
cursor = conn.cursor()

with open(r'D:\Personal Projects\Website\EpicGames Dataset\updated_file.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)  # Skip the header row if it exists

    for row in csvreader:
        title = row[0]
        img_src = row[2]  # Index 2 corresponds to the Image URL field in the CSV
        downloads = row[3]  # Index 2 corresponds to the Image URL field in the CSV
        price = row[4] # Index 4 corresponds to the
        description  = "NULL"
        # genre = row[5] # Index 4 corresponds to the
        publisher = row[6] # Index


        cursor.execute("INSERT INTO games_game (title, image_url, price, publisher, description, downloads) VALUES (?, ?, ?, ?, ?, ?)", (title, img_src, price, publisher, description, downloads))

# table_name = 'games_game'

# cursor.execute(f"DELETE FROM {table_name}")

conn.commit()
conn.close()
