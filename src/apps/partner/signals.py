from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_save
from django.dispatch import receiver
from partner.models import Partner

@receiver(post_save, sender=Partner)
def add_dashboard_access_permission(sender, instance, created, **kwargs):
    # Check if a new Partner instance is created and if the user has a limited role
    if created and instance.role == 'limited':
        # Get the ContentType and Permission objects for the partner app
        content_type = ContentType.objects.get(app_label='partner')
        dashboard_access_perm = Permission.objects.get(
            codename='dashboard_access', content_type=content_type)
        # Add the dashboard_access permission to the user
        instance.users.first().user_permissions.add(dashboard_access_perm)