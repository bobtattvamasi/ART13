#!/usr/bin/env python
import os
import sys

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myapp.settings')

    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise

    # Run the "wait_for_db" management command before running any other command
    # that requires a database connection.
    from django.conf import settings
    if 'wait_for_db' in sys.argv and not settings.DATABASES['default']['HOST']:
        sys.stderr.write("Error: You must provide a 'DB_HOST' environment variable.\n")
        sys.exit(1)

    execute_from_command_line(sys.argv)