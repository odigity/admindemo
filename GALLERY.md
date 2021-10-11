# Gallery

## Page Names

I'm using the following terminology taken from the Django docs:

URL                       | Name
------------------------- | ----------
/admin/                   | Index
/admin/APP/MODEL/         | Changelist
/admin/APP/MODEL/1/change | Change
/admin/APP/MODEL/add      | Add

## Django Admin - Defaults

### Index page, empty

![](gallery/1.png?raw=true)

### Index page, populated

![](gallery/2.png?raw=true)

### Change page for Universe

![](gallery/5.png?raw=true)

### Change page for Universe, with fields = ('name', ('creator', 'birth_year'))

![](gallery/6.png?raw=true)

### Change page for Universe, with fieldsets

![](gallery/7.png?raw=true)

### Change page for Universe, with fieldsets and collapse class (closed)

![](gallery/8.png?raw=true)

### Change page for Universe, with fieldsets and collapse class (open)

![](gallery/9.png?raw=true)

### Change page for Universe, with readonly_fields = ('creator',)

![](gallery/10.png?raw=true)

### Change page for Universe, with save_as = True

![](gallery/11.png?raw=true)

### Change page for Universe, with save_on_top = True

![](gallery/12.png?raw=true)

### Changelist page for Universes, empty

![](gallery/3.png?raw=true)

### Changelist page for Universes, populated

![](gallery/4.png?raw=true)

### Changelist page for Universes, populated, with list_display = ('birth_year', 'name', 'creator')

![](gallery/13.png?raw=true)

### Changelist page for Universes, populated, with list_display = ('birth_year', 'name', 'creator') and list_display_links = None

![](gallery/14.png?raw=true)

### Changelist page for Universes, populated, with list_display = ('birth_year', 'name', 'creator') and list_display_links = ('name',)

![](gallery/15.png?raw=true)

### Changelist page for Universes, populated, with list_display = ('birth_year', 'name', 'creator') and list_editable = ('creator',)

![](gallery/16.png?raw=true)

### Changelist page for Universes, populated, with list_display = ('birth_year', 'name', 'creator') and list_filter = ('birth_year', 'creator')

![](gallery/17.png?raw=true)

### ...clicked to filter creator=Joss+Whedon

![](gallery/17a.png?raw=true)

### Changelist page for Universes, populated, with list_display = ('birth_year', 'name', 'creator') and search_fields = ('name', 'creator')

![](gallery/18.png?raw=true)

### ...searched for 'st'

![](gallery/18a.png?raw=true)

TODO MORE

## Django Admin - Options

TODO

## Package: django-admin-tools

TODO