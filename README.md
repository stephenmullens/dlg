# DLG

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


## Communication:
Data is communicated via POST JSON


## Limitations:
This program is not designed to deal with complex or Decimal numbers.
The precisions IEEE floats has not been evaluated


## Testing:

To run automated tests, cd into the dlg directory and run:

```
python manage.py test
```

This will execute all integration & unit tests and verify operation of the project.


### Integration Testing:
A number of integration tests have been created which:
- Test with a variety of both valid and invalid lists
- verify that failing to include the correct dict key gives an error
- verify GET responds with the appropriate error


### Unit Testing:
The clean_number_list function was created and is being unit tested.
- A large number of tests are performed, but these are not exhaustive.


