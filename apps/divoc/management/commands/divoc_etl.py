from django.core.management.base import BaseCommand, CommandError
from apps.divoc.etl import load_avg_data, load_daily_data, load_total_data

class Command(BaseCommand):
    help = 'Load in DIVOC-91 data files'

    def add_arguments(self, parser):
        parser.add_argument('files', nargs='*', type=str)

    def handle(self, *args, **options):
        if len(options['files']) == 0:
            files = ['total', 'daily', 'avg']  # ORDER MATTERS!
        else: 
            files = options['files']

        if 'total' in files:
            df_total = load_total_data(write_to_db=True)
            print(f"\tTotal: {len(df_total)} records inserted.")
        if 'daily' in files:
            df_daily = load_daily_data(write_to_db=True, debug=False)
            print(f"\Daily: {len(df_daily)} records inserted.")
        if 'avg' in files:
            df_avg = load_avg_data(write_to_db=True, debug=True)
            print(f"\t7d Avg: {len(df_avg)} records inserted.")

    