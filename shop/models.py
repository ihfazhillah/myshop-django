from django.db import models
from django.core.urlresolvers import reverse
from parler.models import TranslatableModel, TranslatedFields
from parler.managers import TranslatableQuerySet, TranslatableManager

# Create your models here.

class Category(TranslatableModel):

    translations = TranslatedFields(
        name = models.CharField(max_length=255,
                                db_index=True),
        slug = models.SlugField(unique=True,
                                max_length=255,
                                db_index=True)
    )


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product-list-by-category', args=[self.slug])

    class Meta:
        # ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class AvailableProductManager(TranslatableManager):
    def all(self):
        return self.get_queryset().filter(is_available=True)

class Product(TranslatableModel):
    category = models.ForeignKey(Category, related_name='products')
    image = models.ImageField(upload_to='products/%Y/%m/%d',
                              blank=True)

    translations = TranslatedFields(
        slug = models.CharField(max_length=255,
                                db_index=True),
        name = models.CharField(max_length=255, db_index=True),
        description = models.TextField()
    )

    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    is_available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    available = AvailableProductManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product-detail', args=[self.id, self.slug])

    class Meta:
        pass
        ordering = ('-created', )
        # index_together = (('id', 'slug'),)

