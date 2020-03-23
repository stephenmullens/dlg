# DLG

A REST endpoint that return the sum of a list of numbers e.g. [1, 2, 3] => 1+2+3 = 6.
The request should be made by POST, and send a JSON object containing the list.

Request (POST):
	{"numbers_to_add": [1, 2, 3}
	content_type='application/json'
	http://localhost:8000/total

Response:
	{
		"total": 6
	}


## Assumptions / Limitations:
This program is not designed to deal with complex or Python Decimal numbers.
The precisions IEEE floats has not been evaluated.
Django places a limit on the size of POST string, this has been manually increased in the settings file.


## Installation - Dev Server

Instructions to clone and run the project from your local machine.

```
	Extract zip
	git clone git@github.com:stephenmullens/dlg.git
	cd dlg
	pipenv install
	pipenv shell
	cd dlg
	python manage.py makemigrations
	python manage.py migrate
	python manage.py runserver
```
Open your web browser to:
http://127.0.0.1:8000/


## Code Styling:
- Python follows the PEP8 standard.
- Linting with flake8


## Testing:

To run automated tests, cd into the dlg directory and run:

```
python manage.py test
```

This will execute all integration & unit tests and verify operation of the project.


### Integration Testing:
A number of integration tests have been created which:
- test a variety of both valid and invalid lists.
- verify that failing to include the correct dict key gives an error.
- verify GET responds with an appropriate error.
- verify that failing to send a list gives an error.

These tests are not exhaustive, and more thought needs to be placed on edge cases.


### Unit Testing:
The clean_number_list function was created and is being unit tested.
- verify that "good" lists are correctly cleaned.
- verify that "bad" lists return False.
