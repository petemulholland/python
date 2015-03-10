rem python ez_setup.py 
rem install virtualenv
easy_install virtualenv

rem setup virtual environment for project:
virtualenv venv

rem activate virtual environment
venv\Scripts\activate

rem Install Flask in virtual environment:
pip install flask

rem install command line parser extension
pip install flask-script

rem Install bootstrap (twitter UI library)
pip install flask-bootstrap


