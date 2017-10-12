clean:
	rm -f collegedataboard.db && python3 buildDB.py

run:
	python3 app.py
