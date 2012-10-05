#!/bin/bash
d=`python -c "import os; print(os.path.dirname(os.path.realpath('$0')))"`
e="$d/env"
s="$d/pypi_server"

[ ! -d "$e" ] && {
	virtualenv "$e"
	source "$e"/bin/activate
	pip install djangopypi
	pip install django
	deactivate
}

source "$e"/bin/activate
cd "$s"
python manage.py syncdb

# http://pypi.python.org/pypi/djangopypi
