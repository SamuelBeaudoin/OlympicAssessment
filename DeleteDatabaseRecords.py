
import sqlite3

con = sqlite3.connect('StockMiniProject.db')

cur = con.cursor()

cur.execute('delete from stockPrices')
con.commit()
con.close()