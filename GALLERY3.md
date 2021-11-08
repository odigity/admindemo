# Gallery3 - django.contrib.admindocs

https://docs.djangoproject.com/en/3.2/ref/contrib/admin/admindocs/

## Screenshots

### Index page

![](gallery3/1.png?raw=true)

### Model Index page

![](gallery3/2.png?raw=true)

### Model Details page

![](gallery3/3.png?raw=true)

### Model Details page, with docstring, verbose_name, and help_text

Source:

    class Universe(models.Model):
        """Docstring for model Universe."""
        name = models.CharField(max_length=30, verbose_name="verbose_name for name", help_text="help_text for name")
        creator = models.CharField(max_length=30, verbose_name="verbose_name for creator", help_text="help_text for creator")
        birth_year = models.IntegerField(verbose_name="verbose_name for birth_year", help_text="help_text for birth_year")

        def my_instance_method(self):
            """Docstring for my_instance_method."""
            pass

        def my_instance_method_with_params(self, param1):
            """Docstring for my_instance_method_with_params."""
            pass

![](gallery3/4.png?raw=true)

