from django.db import models


class Mineral(models.Model):
    name = models.CharField(max_length=255, blank=True, default='')
    image_filename = models.CharField(max_length=255, blank=True, default='')
    image_caption = models.CharField(max_length=255, blank=True, default='')
    category = models.CharField(max_length=255, blank=True, default='')
    formula = models.CharField(max_length=255, blank=True, default='')
    strunz_classification = models.CharField(max_length=255, blank=True,
                                             default='')
    color = models.CharField(max_length=255, blank=True, default='')
    crystal_system = models.CharField(max_length=255, blank=True,
                                      default='')
    unit_cell = models.CharField(max_length=255, blank=True, default='')
    crystal_symmetry = models.CharField(max_length=255, blank=True,
                                        default='')
    cleavage = models.CharField(max_length=255, blank=True, default='')
    mohs_scale_hardness = models.CharField(max_length=255, blank=True,
                                           default='')
    luster = models.CharField(max_length=255, blank=True, default='')
    streak = models.CharField(max_length=255, blank=True, default='')
    diaphaneity = models.CharField(max_length=255, blank=True, default='')
    optical_properties = models.CharField(max_length=255, blank=True,
                                          default='')
    refractive_index = models.CharField(max_length=255, blank=True, default='')
    crystal_habit = models.CharField(max_length=255, blank=True, default='')
    specific_gravity = models.CharField(max_length=255, blank=True, default='')
    group = models.CharField(max_length=255, blank=True, default='')

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name
