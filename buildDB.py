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
    super VARCHAR,
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
    bracket VARCHAR,
    USr VARCHAR,
    niR VARCHAR,
    bvsR VARCHAR,
    ccnR VARCHAR,
    demographics VARCHAR,
    notes VARCHAR
     );''')

conn.execute('''INSERT INTO schools VALUES
    ("Massachusetts Institute of Technology",
    "http://web.mit.edu/",
    "Cambridge, Massachusetts",
    "City",
    "04,476 students (Medium)",
    "Private",
    "07.9%",
    "Early Action",
    "No",
    "Required.<br>one in math (level 1 or 2), and one in science (physics, chemistry, or biology e/m)",
    "770-800",
    "730-780",
    "1500-1580",
    "Yes",
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
    "$17,992",
    "#01",
    "#01",
    "#02",
    "#02",
    "37% White
25% Asian
16% Hispanic
10% Non-resident alien
6% Black
5% Two or more races
2% Unknown
<1% American Indian/Alaska Native",
    "no-fail first year");
''')

conn.execute('''INSERT INTO schools VALUES
    ("Stanford",
    "http://www.stanford.edu/",
    "Stanford, California",
    "Suburban",
    "07,018 students (Medium)",
    "Private",
    "04.8%",
    "Restrictive Early Action (Applicants do not apply to any other <strong>private</strong> college/university under their Early Action, Restrictive Early Action, Early Decision or Early Notification program.)",
    "Yes",
    "Recommended.",
    "700-790",
    "680-780",
    "1380-1570",
    "Yes",
    "5",
    "4",
    "5",
    "4",
    "4",
    "none",
    "none",
    "none",
    "none",
    "4",
    "4",
    "none",
    "none",
    "none",
    "$64,477",
    "$50,547",
    "100%",
    "$18,212",
    "#02",
    "#02",
    "#03",
    "#07",
    "38% White
20% Asian
16% Hispanic
11% Two or more races
8% Non-resident alien
6% Black
1% American Indian/Alaska Native
<1% Native Hawaiian/Pacific Islander
<1% Unknown",
    "");
''')


conn.execute('''INSERT INTO schools VALUES
    ("Carnegie Mellon",
    "http://www.cmu.edu/",
    "Pittsburgh, Pennsylvania",
    "City",
    "05,819 students (Medium)",
    "Private",
    "13.7%",
    "Early Decision",
    "Yes",
    "Recommended.<br>School of Computer Science: Math Level II and
Physics, Chemistry or Biology",
    "700-800",
    "650-750",
    "1350-1550",
    "Yes (SAT only)",
    "4",
    "5",
    "5",
    "4",
    "4",
    "4",
    "5",
    "5",
    "5",
    "none",
    "5",
    "4",
    "5",
    "5",
    "$68,452",
    "$41,636",
    "98%",
    "$29,800",
    "#05",
    "#03",
    "#07",
    "#05",
    "35% White
27% Asian
16% Non-resident alien
8% Hispanic
5% Unknown
5% Black
4% Two or more races
<1% American Indian/Alaska Native
<1% Native Hawaiian/Pacific Islander",
    "Only College of Computer Science");
''')


conn.execute('''INSERT INTO schools VALUES
    ("University of California-Berkeley",
    "http://www.berkeley.edu/",
    "Berkeley, California",
    "City",
    "27,126 students (Large)",
    "Public",
    "17.5%",
    "No",
    "No",
    "Required.<br>College of Chemistry and College of Engineering: Math Level 2 and a science test (Biology E/M, Chemistry, or Physics) closely related to the applicant's intended major.",
    "640-770",
    "610-740",
    "1250-1510",
    "No",
    "3",
    "3",
    "3",
    "3",
    "3",
    "3",
    "3",
    "3",
    "3",
    "3",
    "3",
    "3",
    "3",
    "3",
    "$61,654",
    "$17,284",
    "98.6%",
    "$20,722",
    "#03",
    "#14",
    "#08",
    "#01",
    "35% Asian
28% White
14% Hispanic
14% Non-resident alien
5% Two or more races
3% Unknown
2% Black
<1% Native Hawaiian/Pacific Islander
<1% American Indian/Alaska Native",
    "");
''')


conn.execute('''INSERT INTO schools VALUES
    ("Georgia Institute of Technology",
    "http://www.gatech.edu/",
    "Atlanta, Georgia",
    "City",
    "13,996 students (Medium)",
    "Public",
    "25%",
    "Early Action",
    "Yes",
    "Optional.<br>If you have taken any of these tests before you apply, you are welcome to submit them if you think they support your application.",
    "680-770",
    "630-730",
    "1360-1490",
    "Yes",
    "4",
    "4",
    "4",
    "4",
    "none",
    "4",
    "4",
    "4",
    "4",
    "4",
    "5",
    "none",
    "4",
    "4",
    "$48,566",
    "$13,854",
    "94.0%",
    "$13,736",
    "#06",
    "#08",
    "#04",
    "#04",
    "53% White
19% Asian
11% Non-resident alien
7% Hispanic
6% Black
4% Two or more races
1% Unknown
<1% Native Hawaiian/Pacific Islander
<1% American Indian/Alaska Native",
    "");
''')


conn.execute('''INSERT INTO schools VALUES
    ("Cornell",
    "https://www.cornell.edu/",
    "Ithaca, New York",
    "City",
    "14,195 students (Medium)",
    "Private",
    "14.1%",
    "Early Decision",
    "Yes",
    "Required.<br>Engineering: Mathematics (any level) and a science of your choice<br>Arts and Sciences: Two subjects of your choice",
    "680-770",
    "650-740",
    "1330-1510",
    "Yes (SAT only)",
    "4",
    "4",
    "5",
    "5",
    "none",
    "none",
    "4",
    "4",
    "4",
    "5",
    "5",
    "4",
    "4",
    "4",
    "$67,613",
    "100%",
    "100%",
    "$26,486",
    "#09",
    "#18",
    "#10",
    "#27",
    "42% White
17% Asian
12% Hispanic
10% Non-resident alien
9% Unknown
6% Black
4% Two or more races
<1% American Indian/Alaska Native
<1% Native Hawaiian/Pacific Islander",
    "Computer Science  = College of Arts + Science OR College of Engineering");
''')



conn.execute('''INSERT INTO schools VALUES
    ("University of Michigan",
    "http://www.umich.edu/",
    "Ann Arbor, Michigan",
    "City",
    "28,217 students (Large)",
    "Public",
    "28.6%",
    "Early Action",
    "Yes",
    "Optional.<br>You will not be penalized for low SAT subject test scores since they are not a required component of a complete application.",
    "660-760",
    "620-720",
    "1280-1570",
    "No",
    "5",
    "4",
    "4",
    "4",
    "4",
    "3",
    "4",
    "4",
    "4",
    "5",
    "5",
    "4",
    "4",
    "4",
    "$59,784",
    "89%",
    "95.6%",
    "$18,251",
    "#07",
    "#20",
    "#19",
    "#08",
    "62% White
13% Asian
7% Unknown
7% Non-resident alien
4% Hispanic
4% Black
3% Two or more races
<1% American Indian/Alaska Native
<1% Native Hawaiian/Pacific Islander",
    "Computer Science, Computer Engineering, and Electrical Engineering: College of Engineering");
''')


conn.execute('''INSERT INTO schools VALUES
    ("California Institute of Technology",
    "http://www.caltech.edu/",
    "Pasadena, California",
    "City",
    "01,001 students (Small)",
    "Private",
    "08%",
    "Early Action",
    "Yes",
    "Required.<br>SAT Math Level 2; one science subject test",
    "x",
    "x",
    "x",
    "x",
    "none",
    "none",
    "none",
    "none",
    "none",
    "none",
    "none",
    "none",
    "none",
    "none",
    "none",
    "none",
    "none",
    "none",
    "$68,901",
    "$42,091",
    "55%",
    "$31,931",
    "#10",
    "#05",
    "#99",
    "#03",
    "45% Asian
27% White
12% Hispanic
8% Non-resident alien
5% Two or more races
2% Black
<1% Unknown
<1% American Indian/Alaska Native",
    "placement in courses due to exams; no credit from AP scores");
''')


conn.commit()
conn.close()
