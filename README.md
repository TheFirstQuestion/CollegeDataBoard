# CollegeDataBoard

CollegeDataBoard provides a visualization for college data, in order to better organize and compare information. It was created for personal use only; however, you are free to modify it however you wish.


## Technologies Used

CollegeDataBoard was created primarily to learn Bootstrap and Flask. It also makes use of jQuery and SQLite. `index.html` contains simple JavaScript code to render a GitHub README into HTML.



## Installing

1. Verify that you are running Python 3.

        python3 -V
        python -V

2. Install Flask.

        pip3 install flask
        pip install flask

3. Build the database.

        python3 buildDB.py
        python buildDB.py

4. Run `app.py`

        python3 app.py
        python app.py

5. Visit http://localhost:5000/ in your browser.


## Makefile

You can also use the makefile to install.

1. Create the database: `make clean`

2. Run the app: `make run`

3. Visit http://localhost:5000/ in your browser.
