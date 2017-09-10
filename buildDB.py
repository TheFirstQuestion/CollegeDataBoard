import sqlite3

conn = sqlite3.connect('collegedataboard.db')

conn.execute('''CREATE TABLE schools
    (
    name  VARCHAR       NOT NULL,
    website VARCHAR     NOT NULL,
    location VARCHAR,
    setting VARCHAR,
    size VARCHAR,
    pp VARCHAR,
    rate VARCHAR,
    ED VARCHAR,
    app VARCHAR,
    st VARCHAR,
    SATm VARCHAR,
    SATl VARCHAR,
    SAT VARCHAR,
    sts VARCHAR,
    ABcalc VARCHAR,
    BCcalc VARCHAR,
    chem VARCHAR,
    csa VARCHAR,
    csp VARCHAR,
    gov VARCHAR,
    lang VARCHAR,
    lit VARCHAR,
    econ VARCHAR,
    phy1 VARCHAR,
    phyC VARCHAR,
    stats VARCHAR,
    apush VARCHAR,
    whap VARCHAR,
    tuition VARCHAR,
    avgAid VARCHAR,
    rcvAid VARCHAR,
    bracket VARCHAR
     );''')

conn.execute('''INSERT INTO schools VALUES
    ("Massachusetts Institute of Technology",
    "http://web.mit.edu/",
    "Cambridge, Massachusetts",
    "City",
    "4,476 students (Medium)",
    "Private",
    "7.9%",
    "Early Action",
    "No",
    "two: one in math (level 1 or 2), and one in science (physics, chemistry, or biology e/m)",
    "770-800",
    "730-780",
    "1500-1580",
    "Math: 760-800<br>Science: 740-800",
    "5",
    "5",
    "none",
    "none",
    "none",
    "5",
    "5",
    "5",
    "none",
    "none",
    "5",
    "none",
    "5",
    "5",
    "$67,430",
    "$42,145",
    "91%",
    "$17,992");
''')






conn.commit()
conn.close()
