from django.db import models

''' class SampleModel(models.Model):
    title = models.CharField(max_length=100)
    number = models.IntegerField()
 '''
CATEGORY = (('1','1'),('2','2'),('3','3'),('4','4'),('5','5'))
class PropertyModel(models.Model):
    property_name = models.CharField(max_length=100)
    school_name = models.CharField(max_length=100)
    content = models.TextField()
    postdate = models.DateField(auto_now_add=True)
    evaluation = models.CharField(
        max_length = 50,
        choices = CATEGORY
    )
    address = models.TextField()

    def __str__(self):
        return self.title