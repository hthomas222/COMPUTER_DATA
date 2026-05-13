from flask import Flask, render_template
import sqlite3

app = Flask(__name__)
DB_PATH = 'computers.db'

@app.route("/")
def index():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    rows = conn.execute('SELECT * FROM computers').fetchall()

# CAST the column to a NUMERIC type during the calculation
    stats = conn.execute('''
        SELECT 
            SUM(CAST(price_usd AS NUMERIC)), 
            AVG(CAST(price_usd AS NUMERIC)) 
        FROM computers
    ''').fetchone()
    
    conn.close()
    
    return render_template(
        "index.html", 
        data=rows, 
        total_price=stats[0] or 0, 
        avg_price=stats[1] or 0
    )

if __name__ == '__main__':
    app.run(debug=True)
