#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from pathlib import Path
from dotenv import load_dotenv

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'deliciosoApi.settings')
    try:
        os.environ["API_IS_PROD"] = "1"        
        if(not Path(".env").is_file()):
            load_dotenv("dev.env")
            os.environ["API_IS_PROD"] = "0"
        from django.core.management import execute_from_command_line, commands
        from django.core.management.commands.runserver import Command as runserver
        runserver.default_port = os.getenv('API_PORT')
        if(bool(os.getenv("API_IS_PROD"))):
            runserver.default_addr = "0.0.0.0"
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
