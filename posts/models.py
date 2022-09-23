from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """
    Post model, related to 'owner', i.e. a User instance.
    Default image set so that we can always reference image.url.
    """
    image_filter_choices = [
        # 1st sting in database, 2nd value in dropdown menu
        ('vegetables','vegetables'),
        ('eggs','eggs'),
        ('chicken','chicken'),
        ('pasta','pasta'),
        ('fish','fish'),
        ('bread','bread'),
        ('lamb','lamb'),
        ('fruit','fruit'),
        ('beef','beef'),
        ('cheese','cheese'),
        ('pork','pork'),
        ('rice','rice'),
        ('seafood','seafood'),
        ('goose','goose'),
        ('mussels','mussels'),
        ('chocolate','chocolate'),
        ('game','game'),
        ('duck','duck')  
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='recipe-star-3-api/images/', default='../default_image_upload_fvsf3n', blank=True
    )
    image_filter = models.CharField(
        max_length=32, choices=image_filter_choices, default='normal'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'