import csv, os

from django.core.management.base import BaseCommand
from phones.models import Phone
from django.conf import settings
from django.utils.text import slugify


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open(os.path.join(settings.BASE_DIR, 'phones.csv'), 'r') as csvfile:
            phone_reader = csv.reader(csvfile, delimiter=';')
            # пропускаем заголовок
            next(phone_reader)

            for line in phone_reader:
                # TODO: Добавьте сохранение модели
                id = line[0]
                name = line[1]
                price = line[3]
                image = line[2]
                release_date = line[4]
                lte_exists = line[5]
                slug = slugify(name)

                Phone.objects.create(id=id, name=name, image=image, price=price,
                                     release_date=release_date, lte_exists=lte_exists, slug=slug)
