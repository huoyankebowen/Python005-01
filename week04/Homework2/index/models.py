from django.db import models

# Create your models here.

class CommentStar(models.Model):
    comment_id = models.AutoField(primary_key=True)
    comment = models.CharField(max_length=1000, blank=True, null=True)
    star = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comment_star'