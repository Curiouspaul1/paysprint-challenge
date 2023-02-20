## Instructions To Run

### Pre-Requisites
You need the following to run the app:
- python3
- pip (python's package manager)
- virtualenv library : run `pip install virtualenv` to install

### Steps To Run

- Clone the repository, and cd into the project directory

- create a new virtual environment (optional) using the cmd: `virtualenv <preferred name for virtual environrment>`

- Activate the virtual environment using the command: `.\<virtual env name>\scripts\activate` or for linux `source ./<virtual env name>/bin/activate`

- Once activated run `pip install -r requirements.txt` to install project dependencies

- Next to start the app run `flask run` to begin the web server. Then you can access it via port `5000` on localhost.
