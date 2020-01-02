from django.db import models

class ItemList(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    dob = models.DateField()
    img = models.ImageField(upload_to="images/")
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}".format(self.fname)



