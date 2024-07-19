
![Screenshot (717)](https://github.com/user-attachments/assets/580f2249-0a59-419b-bc3b-1f2da19156d1)
![Screenshot (718)](https://github.com/user-attachments/assets/0adaf7ff-e165-42b1-8bbe-2edf29de68fd)

## Installation

1. Fork this repository to your github account
2. Clone the forked repository and proceed with steps mentioned below

### Install requirements

```
virtualenv env --python=python3.8
source env/bin/activate
pip install -r requirements.txt
```
### Reset DB

```
export FLASK_APP=core/server.py
rm core/store.sqlite3
flask db upgrade -d core/migrations/
```
### Start Server

```
bash run.sh
```
### Run Tests

```
pytest -vvv -s tests/

# for test coverage report
# pytest --cov
# open htmlcov/index.html
```
