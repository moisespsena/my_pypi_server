from django.db import models
from django.db.models.query import QuerySet

class DistributionQueryMixin(object):
    """ Methods that appear both in the manager and queryset. """
    def delete(self):
        # Use individual queries to the attachment is removed.
        for f in self.all():
            f.delete()

class DistributionQuerySet(DistributionQueryMixin, QuerySet):
    pass

class DistributionManager(DistributionQueryMixin, models.Manager):
    def get_query_set(self):
        return DistributionQuerySet(self.model, using=self._db)

