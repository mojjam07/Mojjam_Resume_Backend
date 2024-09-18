from django.core.management.base import BaseCommand
from api.models import Project
from datetime import datetime

class Command(BaseCommand):
    help = 'Adds a new project to the database'

    def handle(self, *args, **kwargs):
        # Create a new project object
        project = Project(
            title='E-Commerce Website',
            description='A market place website.',
            technologies='Django (HTML-templates & CSS/JS-static)',
            github_link='https://github.com/example/ecommerce-project',
            image='image_link.png',
            created_at=datetime.now()
        )

        # Save the project to the database
        project.save()

        self.stdout.write(self.style.SUCCESS(f"Project '{project.title}' added successfully"))
