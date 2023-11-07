import sqlite3
import csv

conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

with open(r'D:\Practice\Web Scrape\game_details.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)  # Skip the header row if it exists

    for row in csvreader:
        title = row[0]
        image_url = row[2]  # Index 2 corresponds to the Image URL field in the CSV
        image_cover_url = row[3] # Index 3 corresponds to the
        price = row[4] # Index 4 corresponds to the
        publisher = row[5] # Index
        description = row[6] # Index


        cursor.execute("INSERT INTO games_game (title, image_url, image_cover_url, price, publisher, Description) VALUES (?, ?, ?, ?, ?, ?)", (title, image_url, image_cover_url, price, publisher, description))

# table_name = 'games_game'

# cursor.execute(f"DELETE FROM {table_name}")

conn.commit()
conn.close()
