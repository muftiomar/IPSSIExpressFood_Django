from django.core.management.base import BaseCommand
from pymongo import MongoClient
from django.conf import settings

class Command(BaseCommand):
    help = 'Test the MongoDB database connection'

    def handle(self, *args, **kwargs):
        client = None
        try:
            # Extract MongoDB connection details
            db_settings = settings.DATABASES['default']
            host = db_settings['CLIENT']['host']

            # Connect to MongoDB using pymongo directly
            client = MongoClient(host)

            # Test connection by listing databases (or any simple operation)
            client.admin.command('ping')
            self.stdout.write(self.style.SUCCESS('Database connection successful!'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Database connection failed: {e}'))

        finally:
            if client:
                client.close()
