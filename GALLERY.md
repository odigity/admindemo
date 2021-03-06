# Gallery - Django Admin - Native

## Page Names

I'm using the following terminology taken from the Django docs:

URL                       | Name
------------------------- | ----------
/admin/                   | Index
/admin/APP/               | App Index
/admin/APP/MODEL/         | Changelist
/admin/APP/MODEL/1/change | Change
/admin/APP/MODEL/add      | Add

## Screnshots

### Index page, empty

![](gallery/1.png?raw=true)

### Index page, empty - with custom index_title/site_header/site_title and site_url = None

![](gallery/31.png?raw=true)

### Index page, populated

![](gallery/2.png?raw=true)

### App Index page

![](gallery/32.png?raw=true)

### Changelist page for Universes, empty

![](gallery/3.png?raw=true)

### Changelist page for Universes, populated

![](gallery/4.png?raw=true)

### Changelist page for Universes, with list_display = [ 'birth_year', 'name', 'creator' ]

![](gallery/13.png?raw=true)

### Changelist page for Universes, with list_display = [ 'birth_year', 'name', 'creator' ] and ordering = ['name']

![](gallery/21.png?raw=true)

### Changelist page for Universes, with list_display = [ 'birth_year', 'name', 'creator' ] and list_display_links = None

![](gallery/14.png?raw=true)

### Changelist page for Universes, with list_display = [ 'birth_year', 'name', 'creator' ] and list_display_links = [ 'name' ]

![](gallery/15.png?raw=true)

### Changelist page for Universes, with list_display = [ 'birth_year', 'name', 'creator' ] and list_editable = [ 'creator' ]

![](gallery/16.png?raw=true)

### Changelist page for Universes, with list_display = [ 'birth_year', 'name', 'creator' ] and list_filter = [ 'birth_year', 'creator' ]

![](gallery/17.png?raw=true)

### ...clicked to filter creator=Joss+Whedon

![](gallery/17a.png?raw=true)

### Changelist page for Universes, with list_display = [ 'birth_year', 'name', 'creator' ] and search_fields = [ 'name', 'creator' ]

![](gallery/18.png?raw=true)

### ...searched for 'st'

![](gallery/18a.png?raw=true)

### Change page for Universe

![](gallery/5.png?raw=true)

### Change page for Universe, with fields = [ 'name', ('creator', 'birth_year') ]

![](gallery/6.png?raw=true)

### Change page for Universe, with fieldsets

![](gallery/7.png?raw=true)

### Change page for Universe, with fieldsets and collapse class (closed)

![](gallery/8.png?raw=true)

### Change page for Universe, with fieldsets and collapse class (open)

![](gallery/9.png?raw=true)

### Change page for Universe, with readonly_fields = [ 'creator' ]

![](gallery/10.png?raw=true)

### Change page for Universe, with save_as = True

![](gallery/11.png?raw=true)

### Change page for Universe, with save_on_top = True

![](gallery/12.png?raw=true)

### Change page for Universe, with inline = [ Character(Tabular) ]

![](gallery/33a.png?raw=true)
![](gallery/33b.png?raw=true)

### Change page for Universe, with inline = [ Character(Tabular, extra = 0) ]

![](gallery/34b.png?raw=true)

### Change page for Universe, with inline = [ Character(Tabular, has_change_permission -> False) ]

![](gallery/35.png?raw=true)

### Change page for Universe, with inline = [ Character(Tabular, has_change_permission -> False, show_change_link = True) ]

![](gallery/36.png?raw=true)

### Change page for Universe, with inline = [ Character(Tabular, show_change_link = True) ]

![](gallery/37.png?raw=true)

### Change page for Universe, with inline = [ Character(Tabular, fields = [ 'name', 'friends' ]) ]

![](gallery/38.png?raw=true)

### Change page for Universe, with inline = [ Character(Tabular, fields = [ 'name', 'friends' ], readonly_fields = [ 'friends' ]) ]

![](gallery/39.png?raw=true)

### Change page for Universe, with inline = [ Character(Stacked) ]

![](gallery/40a.png?raw=true)
![](gallery/40b.png?raw=true)

### Change page for Universe, with inline = [ Character(Stacked, show_change_link = True) ]

![](gallery/41.png?raw=true)

### Change page for Universe, with inline = [ Character(Stacked, show_change_link = True, has_change_permission -> False) ]

![](gallery/42.png?raw=true)

### Change page for Universe, with inline = [ Character(Stacked, fields = [ 'name', 'friends' ], readonly_fields = [ 'friends' ]) ]

![](gallery/43.png?raw=true)

### Changelist page for Units of Fiction

![](gallery/22.png?raw=true)

### Changelist page for Units of Fiction, with date_hierarchy = 'pub_date'

![](gallery/23.png?raw=true)

### ...clicked to filter on '1997'

![](gallery/24.png?raw=true)

### ...clicked to filter on 'March 1997'

![](gallery/25.png?raw=true)

### Changelist page for Units of Fiction, with date_hierarchy = 'pub_date' and list_filter = [ 'pub_date' ]

![](gallery/26.png?raw=true)

### Changelist page for Units of Fiction, with date_hierarchy = 'pub_date' and list_filter = [ 'pub_date', 'medium', 'universe', 'length' ]

![](gallery/27.png?raw=true)

### Changelist page for Units of Fiction, with list_display = [ 'universe', 'ordinal', 'title', 'pub_date' ]

![](gallery/28.png?raw=true)

### Changelist page for Units of Fiction, with list_display = [ 'universe', 'ordinal', 'title', 'pub_date' ] and ordering = [ 'universe', 'ordinal' ]

![](gallery/29.png?raw=true)

### Changelist page for Units of Fiction, with list_display = [ 'universe_name', 'ordinal', 'title', 'pub_date' ] and ordering = [ 'universe__name', 'ordinal' ]

(`universe_name` -> custom method on UnitOfFiction model)

![](gallery/30.png?raw=true)
