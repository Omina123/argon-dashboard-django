# initialize_data.py

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'argon-dashboard-django.settings')
django.setup()

from authentication.models import Course, Unit

def initialize_data():
    # Create Computer Science course
    computer_science = Course.objects.create(name="Computer Science", code="CS")
    # Create units for Computer Science
    Unit.objects.create(name="Introduction to Programming", code="CS101", course=computer_science)
    Unit.objects.create(name="Data Structures", code="CS102", course=computer_science)

    # Create Health Science course
    health_science = Course.objects.create(name="Health Science", code="HS")
    # Create units for Health Science
    Unit.objects.create(name="Anatomy", code="HS101", course=health_science)
    Unit.objects.create(name="Physiology", code="HS102", course=health_science)

    # Add more courses and units as needed

if __name__ == "__main__":
    initialize_data()
