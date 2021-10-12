See [Gallery](GALLERY.md) for screenshots.

## Dev Cycle

* _(skip first time)_ `rm db.sqlite3 worlds/migrations/0001_initial.py; ./manage.py makemigrations`
* `./manage.py migrate; ./manage.py loaddata worlds/examples`
* `./manage.py runserver`

## Schema

```
worlds_character
    id                      integer     NOT NULL PRIMARY KEY AUTOINCREMENT
    name                    varchar(30) NOT NULL
    universe_id             bigint      NOT NULL REFERENCES "worlds_universe" ("id")

worlds_character_appearances
    id                      integer     NOT NULL PRIMARY KEY AUTOINCREMENT
    character_id            bigint      NOT NULL REFERENCES "worlds_character" ("id")
    unitoffiction_id        bigint      NOT NULL REFERENCES "worlds_unitoffiction" ("id")

worlds_character_friends
    id                      integer     NOT NULL PRIMARY KEY AUTOINCREMENT
    from_character_id       bigint      NOT NULL REFERENCES "worlds_character" ("id")
    to_character_id         bigint      NOT NULL REFERENCES "worlds_character" ("id")

worlds_episode
    unitoffiction_ptr_id    bigint      NOT NULL PRIMARY KEY REFERENCES "worlds_unitoffiction" ("id")
    number                  varchar(10) NOT NULL
    series_id               bigint      NOT NULL REFERENCES "worlds_series" ("id")

worlds_medium
    id                      integer     NOT NULL PRIMARY KEY AUTOINCREMENT
    label                   varchar(30) NOT NULL
    parent_id               bigint      NULL REFERENCES "worlds_medium" ("id")

worlds_series
    id                      integer     NOT NULL PRIMARY KEY AUTOINCREMENT
    title                   varchar(30) NOT NULL
    universe_id             bigint      NOT NULL REFERENCES "worlds_universe" ("id")

worlds_unitoffiction
    id                      integer     NOT NULL PRIMARY KEY AUTOINCREMENT
    title                   varchar(80) NOT NULL
    length                  integer     NULL
    pub_date                datetime    NOT NULL
    medium_id               bigint      NOT NULL REFERENCES "worlds_medium" ("id")
    universe_id             bigint      NOT NULL REFERENCES "worlds_universe" ("id")
    _order                  integer     NOT NULL

worlds_universe
    id                      integer     NOT NULL PRIMARY KEY AUTOINCREMENT
    name                    varchar(30) NOT NULL
    creator                 varchar(30) NOT NULL
    birth_year              integer     NOT NULL
```
