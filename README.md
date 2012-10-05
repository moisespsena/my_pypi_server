# My PyPI Server

My Local Python PyPI Server Repository with [Django](https://github.com/django/django) and [DjangoPyPI](https://github.com/benliles/djangopypi).

## Installation

```bash
git clone https://github.com/moisespsena/my_pypi_server my_pypi_server
cd my_pypi_server
./install.sh
```

## Run Server

```bash
my_pypi_server/run-server.sh
```

Usage:

```bash
./run-server.sh --help

Usage: manage.py runserver [options] [optional port number, or ipaddr:port]

Starts a lightweight Web server for development and also serves static files.

Options:
  -v VERBOSITY, --verbosity=VERBOSITY
                        Verbosity level; 0=minimal output, 1=normal output,
                        2=verbose output, 3=very verbose output
  --settings=SETTINGS   The Python path to a settings module, e.g.
                        "myproject.settings.main". If this isn't provided, the
                        DJANGO_SETTINGS_MODULE environment variable will be
                        used.
  --pythonpath=PYTHONPATH
                        A directory to add to the Python path, e.g.
                        "/home/djangoprojects/myproject".
  --traceback           Print traceback on exception
  -6, --ipv6            Tells Django to use a IPv6 address.
  --nothreading         Tells Django to NOT use threading.
  --noreload            Tells Django to NOT use the auto-reloader.
  --nostatic            Tells Django to NOT automatically serve static files
                        at STATIC_URL.
  --insecure            Allows serving static files even if DEBUG is False.
  --version             show program's version number and exit
  -h, --help            show this help message and exit
```
