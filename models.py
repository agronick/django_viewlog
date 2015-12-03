from django.db import models
from django.contrib.auth.models import User

class PageLog(models.Model):
    user = models.ForeignKey(User, blank=True, null=True)
    path = models.CharField(max_length=512)
    request_type = models.CharField(max_length=5)
    referrer = models.CharField(max_length=512)
    status_code = models.PositiveSmallIntegerField()
    date = models.DateTimeField(auto_now_add=True)
     
    def count(self):
        return ViewLog.objects.filter(path=self.path).count()
 