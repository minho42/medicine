import sqlite3
from wiki import wiki_summary

def run():
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    cursor.execute(
        '''CREATE TABLE IF NOT EXISTS medications
        (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
        name TEXT UNIQUE NOT NULL, 
        wiki TEXT)'''
        )
    with open('medication_list.txt', 'r') as file:
        for line in file:
            name = line.strip()
            # strip name after "(" or "," for wiki
            # e.g.
            # Aspirin (analgesic)	
            # Lignocaine, see Lidocaine (anaesthesia)
            name_for_wiki = name.split('(')[0].split(',')[0].strip()
            wiki = wiki_summary(name_for_wiki)
            print(f"{name_for_wiki}: {wiki[:20]}...")
            
            cursor.execute(
                '''INSERT OR REPLACE INTO medications (name, wiki)
                VALUES (?, ?)''', (name, wiki)
            )
            
    conn.commit()
    conn.close()
            
if __name__ == "__main__":
    run()
