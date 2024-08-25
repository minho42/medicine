import sqlite3
from wiki import wiki_summary

def run():
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    cursor.execute(
        '''CREATE TABLE IF NOT EXISTS medications
        (name TEXT PRIMARY KEY, wiki TEXT)'''
        )
    with open('medication_list.txt', 'r') as file:
        for line in file:
            name = line.strip()
            wiki = wiki_summary(name)
            print(f"{name}: {wiki[:20]}...")
            
            cursor.execute(
                '''INSERT OR REPLACE INTO medications (name, wiki)
                VALUES (?, ?)''', (name, wiki)
            )
            
    conn.commit()
    conn.close()
            
if __name__ == "__main__":
    run()
