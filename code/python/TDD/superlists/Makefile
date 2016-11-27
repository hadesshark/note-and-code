unittest:
	python3 manage.py test lists 2> stderr.txt

functiontest:
	python3 manage.py test functional_tests 2> stderr.txt

run:
	python3 manage.py runserver

migrate:
	rm db.sqlite3
	python3 manage.py migrate --noinput
