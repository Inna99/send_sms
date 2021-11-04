echo STARTING BLACK
black .
echo STARTING FLAKE8
flake8 .
flake8 tests
echo STARTING ISORT
isort --check .
isort .
echo RUNNING TESTS
py.test tests