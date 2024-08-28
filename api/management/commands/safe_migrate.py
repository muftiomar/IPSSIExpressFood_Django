# File: api/management/commands/safe_migrate.py
from django.core.management.commands.migrate import Command as MigrateCommand
from django.db import connections

class Command(MigrateCommand):
    def handle(self, *args, **options):
        try:
            super().handle(*args, **options)
        finally:
            # Manually close connections without triggering errors
            for conn in connections.all():
                if conn.connection is not None:
                    try:
                        conn.close()
                    except Exception as e:
                        print("Error closing the connection:", e)
