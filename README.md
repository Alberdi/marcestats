# marcestats
Board game plays database ~~and visualizations~~.

## Goals

At the moment, I'm more concerned with modelling and storing all my plays in a database than displaying them in a pretty web page. I'd be great to have fancy charts, but in the meantime I'd be using it as a glorified spreadsheet and tapping into the database via raw SQL and Django queries.

If you're looking for something else, [NemeStats](https://github.com/NemeStats/NemeStats) is also free software and has a very nice UI. I created this project because NemeStats didn't fit my personal requirements regarding the underlying model (factions, teams, etc.).

## Installation

* Clone this repository: `git clone https://github.com/Alberdi/marcestats.git`
* Run the setup scripts: `python manage.py migrate`
* Create a superuser: `python manage.py createsuperuser`
* Run the server: `python manage.py runserver`

You can then use the `/admin` panel to populate your database with information about your board game plays and use the main website to see stats about them.

Feel free to collaborate as you see fit :)
