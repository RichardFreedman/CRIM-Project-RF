from django.db import models
from django.utils.text import slugify

from crim.models.person import CRIMPerson
from crim.models.piece import CRIMPiece


class CRIMRelationshipType(models.Model):
    class Meta:
        app_label = 'crim'
        verbose_name = 'Relationship type'
        verbose_name_plural = 'Relationship types'

    relationship_type_id = models.SlugField(
        max_length=32,
        unique=True,
        db_index=True,
    )
    name = models.CharField(max_length=32)
    remarks = models.TextField('remarks (supports Markdown)', blank=True)

    def __str__(self):
        return '{0}'.format(self.name)

    def _get_unique_slug(self):
        slug_base = slugify(self.name)
        unique_slug = slug_base
        num = 1
        while CRIMRelationshipType.objects.filter(relationship_type_id=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug_base, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        # Create unique id based on the name
        if not self.relationship_type_id:
            self.relationship_type_id = self._get_unique_slug()
        # Finalize changes
        super().save()


class CRIMMusicalType(models.Model):
    class Meta:
        app_label = 'crim'
        verbose_name = 'Musical type'
        verbose_name_plural = 'Musical types'

    musical_type_id = models.SlugField(
        max_length=32,
        unique=True,
        db_index=True,
    )
    name = models.CharField(max_length=32)
    remarks = models.TextField('remarks (supports Markdown)', blank=True)

    def __str__(self):
        return '{0}'.format(self.name)

    def _get_unique_slug(self):
        slug_base = slugify(self.name)
        unique_slug = slug_base
        num = 1
        while CRIMMusicalType.objects.filter(musical_type_id=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug_base, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        # Create unique id based on the name
        if not self.musical_type_id:
            self.musical_type_id = self._get_unique_slug()
        # Finalize changes
        super().save()


class CRIMRelationship(models.Model):
    class Meta:
        app_label = 'crim'
        verbose_name = 'Relationship'
        verbose_name_plural = 'Relationships'

    relationship_id = models.SlugField(
        max_length=64,
        unique=True,
    )

    observer = models.ForeignKey(
        CRIMPerson,
        on_delete=models.SET_NULL,
        to_field='person_id',
        null=True,
        db_index=True,
        related_name='relationships',
    )

    relationship_type = models.ForeignKey(
        CRIMRelationshipType,
        on_delete=models.SET_NULL,
        to_field='relationship_type_id',
        null=True,
        db_index=True,
    )

    model = models.ForeignKey(
        CRIMPiece,
        on_delete=models.CASCADE,
        to_field='piece_id',
        db_index=True,
        related_name='relationships_as_model',
    )
    model_ema = models.TextField()
    model_musical_types = models.ManyToManyField(
        CRIMMusicalType,
        db_index=True,
        related_name='relationships_as_model'
    )

    derivative = models.ForeignKey(
        CRIMPiece,
        on_delete=models.CASCADE,
        to_field='piece_id',
        db_index=True,
        related_name='relationships_as_derivative',
    )
    derivative_ema = models.TextField()
    derivative_musical_types = models.ManyToManyField(
        CRIMMusicalType,
        db_index=True,
        related_name='relationships_as_derivative'
    )

    remarks = models.TextField('remarks (supports Markdown)', blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{0}'.format(self.relationship_id)

    def _get_unique_slug(self):
        slug_base = (self.model.piece_id + '-' + self.derivative.piece_id)
        num = 1
        unique_slug = '{}-{}'.format(slug_base, num)
        while CRIMRelationship.objects.filter(relationship_id=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug_base, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        # Create unique id based on the name
        if not self.relationship_id:
            self.relationship_id = self._get_unique_slug()
        # Finalize changes
        super().save()
