from django.core.management.base import BaseCommand, CommandError
from apps.vaccine.etl import load_data

class Command(BaseCommand):
    help = 'Load in DIVOC-91 data files'


    def handle(self, *args, **options):
        df = load_data(write_to_db=True)
        print(f"\tVaccines: {len(df)} records inserted.")
        