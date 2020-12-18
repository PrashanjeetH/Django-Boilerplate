from django.core.management.base import BaseCommand
import os


class Command(BaseCommand):
    help = 'Renames a Django Project'

    def add_arguments(self, parser):
        parser.add_argument('new_project_name', type=str, help='The New Django project name')

        # parser.add_argument('-p', '--prefix')

    def handle(self, *args, **kwargs):
        new_project_name = kwargs['new_project_name']

        # Logic to rename files

        files_to_rename = ['boilerplate/settings/base.py', 'boilerplate/wsgi.py', 'manage.py', 'boilerplate/asgi.py', ]
        folder_to_rename = 'boilerplate'

        for file_name in files_to_rename:
            with open(file_name, 'r') as file:
                file_data = file.read()
            file_data = file_data.replace('demo', new_project_name)
            with open(file_name, 'w') as file_to_write:
                file_to_write.write(file_data)
            file_to_write.close()
            file.close()

        os.rename(folder_to_rename, new_project_name)

        self.stdout.write(self.style.SUCCESS(f'Project has been renamed as {new_project_name}'))
