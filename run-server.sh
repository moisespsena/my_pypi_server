#!/bin/bash
d=`python -c "import os; print(os.path.dirname(os.path.realpath('$0')))"`
e="$d/env"
s="$d/pypi_server"

source "$e"/bin/activate && \
    cd "$s" && \
    python manage.py runserver "$@"
