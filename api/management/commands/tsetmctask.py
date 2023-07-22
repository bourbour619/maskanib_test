from django.core.management.base import BaseCommand, CommandError
from api.tasks import tsetmc_indexes_with_histories


class Command(BaseCommand):
    help = "Run tsetmc task for retrieve and update database"

    def add_arguments(self, parser):
        parser.add_argument(
            "--update",
            action="store_true",
            help="Run tsetmc task just for update",
        )

    def handle(self, *args, **options):
        update = options.get('update')
        tsetmc_indexes_with_histories.delay(update)
        self.stdout.write(
            self.style.SUCCESS('Done, runserver and enjoy the api :)')
        )
