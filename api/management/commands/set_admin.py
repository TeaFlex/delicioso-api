import os
from typing import Any, Optional
from django.core.management import BaseCommand
from django.contrib.auth.models import User

ADMIN_USERNAME = os.getenv("API_ADMIN_UNAME")
ADMIN_PASSWORD = os.getenv("API_ADMIN_PWD")

class Command(BaseCommand):

    help = "Create the admin user"

    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        self.stdout.write(self.style.MIGRATE_HEADING(self.help))
        self.stdout.write(self.style.WARNING(f"Attempting to create user \"{ADMIN_USERNAME}\"..."))

        u = User.objects.filter(id=1)
        if(u.exists() and u.first().is_superuser):
            current_admin = u.first()
            self.stdout.write(self.style.WARNING(f"User \"{current_admin}\" is already the super user, passing..."))
            return

        if(u.exists() and not u.first().is_superuser):
            self.stderr.write(self.style.ERROR(f"The first user is not super user."))
            return
        
        User.objects.create_superuser(ADMIN_USERNAME, "admin@admin.com", ADMIN_PASSWORD)
        self.stdout.write(self.style.SUCCESS("Super user created !"))