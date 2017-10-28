from django.db import models

class AbstractTimeStampedModel(models.Model):
    '''Abstract model class for automatic addition of
    create/modified timestamps '''

    # A timestamp representing when this object was created.
    created = models.DateTimeField(auto_now_add=True)

    # A timestamp reprensenting when this object was last updated.
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

        # By default, any model that inherits from `TimestampedModel` should
        # be ordered in reverse-chronological order. We can override this on a
        # per-model basis as needed, but reverse-chronological is a good
        # default ordering for most models.
        ordering = ['-created', '-modified']
