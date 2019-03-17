PROJECT = rest_api
PROJECT_DESCRIPTION = Marcestats REST API
PROJECT_VERSION = 0.1.0

# Whitespace to be used when creating files from templates.
SP = 4

DEPS = cowboy esqlite jiffy
dep_cowboy_commit = 2.6.1
dep_esqlite = hex 0.3.0

DEP_PLUGINS = cowboy

include erlang.mk

DB_PATH = "$(shell pwd)/../db.sqlite3"
define PROJECT_ENV
[
    {dbpath, $(DB_PATH)}
]
endef
