import sqlite3

def data():
    conn = sqlite3.connect('computers.db')
    c = conn.cursor()
    c.execute('''
    CREATE TABLE IF NOT EXISTS computers (
    id INTEGER PRIMARY KEY,
    model TEXT,
    manufacturer TEXT,
    release_year INTEGER,
    cpu_model TEXT,
    cpu_cores INTEGER,
    cpu_base_ghz REAL,
    ram_gb INTEGER,
    storage_gb INTEGER,
    storage_type TEXT,
    gpu_model TEXT,
    os TEXT,
    price_usd REAL,
    passmark_cpu INTEGER,
    notes TEXT
    )''')

    rows = [
    (1,'ThinkPad X1 Carbon 9','Lenovo',2021,'Intel Core i7-1165G7',4,2.8,16,512,'SSD','Intel Iris Xe','Windows 10',1799,12400,'Ultrabook, business'),
    (2,'MacBook Pro 16 2019','Apple',2019,'Intel Core i9-9980HK',8,2.4,32,1000,'SSD','AMD Radeon Pro 5500M','macOS',2399,16800,'High-end creative'),
    (3,'XPS 13 9310','Dell',2021,'Intel Core i7-1185G7',4,3.0,16,512,'SSD','Intel Iris Xe','Windows 10',1499,12200,'Compact'),
    (4,'ROG Strix G15','ASUS',2021,'AMD Ryzen 9 5900HX',8,3.3,32,1000,'SSD','NVIDIA RTX 3070','Windows 10',1899,21500,'Gaming laptop'),
    (5,'Inspiron 15 3000','Dell',2020,'Intel Core i3-1005G1',2,1.2,8,256,'SSD','Intel UHD','Windows 10',399,5200,'Budget'),
    (6,'Surface Laptop 4','Microsoft',2021,'AMD Ryzen 7 4980U',8,2.0,16,512,'SSD','Integrated','Windows 10',1299,12000,'2-in-1 style'),
    (7,'Legion 5','Lenovo',2020,'AMD Ryzen 7 4800H',8,2.9,16,1000,'SSD','NVIDIA GTX 1660 Ti','Windows 10',999,14500,'Gaming'),
    (8,'MacBook Air M1','Apple',2020,'Apple M1',8,3.2,8,512,'SSD','Integrated','macOS',999,17000,'Fanless, efficient'),
    (9,'ThinkCentre M90n','Lenovo',2019,'Intel Core i5-8265U',4,1.6,8,256,'SSD','Integrated','Windows 10',749,9400,'Mini desktop'),
    (10,'HP ProBook 450','Gigabyte',2018,'Intel Core i5-8250U',4,1.6,8,500,'HDD','Integrated','Windows 10',649,8600,'Business laptop'),
    (11,'Custom Desktop GTX 1660','Custom',2020,'Intel Core i5-10400F',6,2.9,16,2000,'HDD','NVIDIA GTX 1660','Windows 10',899,14000,'Midrange gaming build'),
    (12,'Workstation Z4','HP',2019,'Intel Xeon W-2123',4,3.6,32,2000,'SSD','NVIDIA Quadro P2000','Windows 10 Pro',2499,19500,'Professional CAD')
    ]

    c.executemany('INSERT OR REPLACE INTO computers VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', rows)
    conn.commit()
    conn.close()
data()
print('computers.db created with sample data')
