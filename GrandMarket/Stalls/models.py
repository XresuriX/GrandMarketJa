from django.db import models
from django.utils.translation import gettext_lazy as _
from oscar.core.compat import AUTH_USER_MODEL
from PIL import Image
from django.urls import reverse
from oscar.core.utils import get_default_currency
from django.utils.functional import cached_property


class Stall(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(null=True, max_length=200, default='download.png', upload_to='images/stall_img')
    owner = models.OneToOneField(
        AUTH_USER_MODEL, related_name="customeuser", unique=True, on_delete=models.CASCADE,
        blank=True, verbose_name=_("Manager"))
    primary_delivery_location = models.CharField(max_length=150, blank=True, null=True)
    secondary_delivery_location = models.CharField(max_length=150, blank=True, null=True)
    phone = models.CharField(max_length=20, null=True, blank=True)

    class Meta:
        app_label = 'Stalls'

    def get_absolute_url(self):
        return reverse('Stalls:details', kwargs={'pk': self.id})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class StallStock(models.Model):
    owner = models.ForeignKey(
        'Stall',
        on_delete=models.CASCADE,
        verbose_name=_("owner"),
        related_name='customuser')
    product = models.ForeignKey(
        'catalogue.Product',
        on_delete=models.CASCADE,
        related_name="stallstockrecords",
        verbose_name=_("Product"))
    # Price info:
    price_currency = models.CharField(
        _("Currency"), max_length=12, default=get_default_currency)
    # Price info:
    price_currency = models.CharField(
        _("Currency"), max_length=12, default=get_default_currency)

    # This is the base price for calculations - whether this is inclusive or exclusive of
    # tax depends on your implementation, as this is highly domain-specific.
    # It is nullable because some items don't have a fixed
    # price but require a runtime calculation (possibly from an external service).
    price = models.DecimalField(
        _("Price"), decimal_places=2, max_digits=12,
        blank=True, null=True)

    #: Number of items in stock
    num_in_stock = models.PositiveIntegerField(
        _("Number in stock"), blank=True, null=True)

    #: The amount of stock allocated to orders but not fed back to the master
    #: stock system.  A typical stock update process will set the
    #: :py:attr:`.num_in_stock` variable to a new value and reset
    #: :py:attr:`.num_allocated` to zero.
    num_allocated = models.IntegerField(
        _("Number allocated"), blank=True, null=True)

    #: Threshold for low-stock alerts.  When stock goes beneath this threshold,
    #: an alert is triggered so warehouse managers can order more.
    low_stock_threshold = models.PositiveIntegerField(
        _("Low Stock Threshold"), blank=True, null=True)

    # Date information
    date_created = models.DateTimeField(_("Date created"), auto_now_add=True)
    date_updated = models.DateTimeField(_("Date updated"), auto_now=True,
                                        db_index=True)

    class Meta:
        app_label = 'Stalls'
        verbose_name = _("Stall Stock")
        verbose_name_plural = _("Stall Stocks")

    @property
    def net_stock_level(self):
        """
        The effective number in stock (e.g. available to buy).
        This is correct property to show the customer, not the
        :py:attr:`.num_in_stock` field as that doesn't account for allocations.
        This can be negative in some unusual circumstances
        """
        if self.num_in_stock is None:
            return 0
        if self.num_allocated is None:
            return self.num_in_stock
        return self.num_in_stock - self.num_allocated

    @cached_property
    def can_track_allocations(self):
        """Return True if the Product is set for stock tracking."""
        return self.product.get_product_class().track_stock
