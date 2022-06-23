import yfinance as yf
import sqlite3

con = sqlite3.connect('StockMiniProject.db')

cur = con.cursor()

#CODE USED TO CREATE THE SQLITE TABLE
cur.execute('''CREATE TABLE stockPrices
               (Date text, Open real, Close real, High real, Low real)''')
con.commit()
con.close()

ticker = "LBS=F"

data = yf.download(ticker, "2020-01-01", "2022-01-01", interval='1d')
data.dropna(inplace=True, how="all")
data = data.reset_index()#.to_dict(orient='list')
print(data)
for index, row in data.iterrows():
    con = sqlite3.connect('StockMiniProject.db')
    cur = con.cursor()

    cur.execute("INSERT INTO stockPrices VALUES (?, ?, ?, ?, ?)", (str(row[0])[0:10], row[1], row[2], row[3], row[4]))
    con.commit()
    con.close()


