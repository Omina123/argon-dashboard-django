from django.core.management.base import BaseCommand
from home.models import Course, Unit

class Command(BaseCommand):
    help = 'Initializes data for courses and units'

    def handle(self, *args, **kwargs):
        # Create Computer Science course
        computer_science = Course.objects.create(name="Computer Science")
        # Create units for Computer Science
        Unit.objects.create(name="Introduction to Programming", course=computer_science)
        Unit.objects.create(name="Data Structures", course=computer_science)

        # Create Health Science course
        health_science = Course.objects.create(name="Health Science")
        # Create units for Health Science
        Unit.objects.create(name="Anatomy", course=health_science)
        Unit.objects.create(name="Physiology", course=health_science)
        
        # Repeat this process for other courses and units

        self.stdout.write(self.style.SUCCESS('Data initialized successfully'))
