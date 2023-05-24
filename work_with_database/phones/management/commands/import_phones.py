import csv

from django.core.management.base import BaseCommand

from phones.models import Phone


class Command(BaseCommand):
    help = 'Import phones from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to CSV-file')

    def handle(self, *args, **options):
        csv_file = options['csv_file']
        with open(csv_file, encoding='UTF-8') as f:
            reader = csv.DictReader(f, delimiter=';')
            for row in reader:
                phone = Phone(
                    name=row['name'],
                    price=float(row['price']),
                    image=row['image'],
                    release_date=row['release_date'],
                    lte_exists=bool(row['lte_exists']),
                )
                phone.save()

