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
    ACTc VARCHAR,
    ACTs VARCHAR,
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
    phy2 VARCHAR,
    phyC VARCHAR,
    stats VARCHAR,
    apush VARCHAR,
    whap VARCHAR
     );''')







conn.commit()
conn.close()
