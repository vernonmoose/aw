from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

def healthTip_directory_path(instance, filename):
    return 'HealthTips/tip_{0}/{1}'.format(instance.id, filename)

class HealthTip(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    image = models.ImageField(blank=True, null=True, upload_to=healthTip_directory_path)

    def __str__(self):
        return self.title
    
class Paragraph(models.Model):
    tip = models.ForeignKey(HealthTip, related_name='paragraphs', on_delete=models.CASCADE)
    content = models.TextField()
    order = models.PositiveIntegerField()
    
    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"Paragraph {self.order} of {self.blog_post.title}"