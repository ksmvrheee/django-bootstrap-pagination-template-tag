## Overview
This is yet another realization of pagination-creating template tag for Django. It uses Bootstrap 5 classes, but it can be adapted and customized with your own css because it doesn't use too many classes. The pagination block is compatible with screen readers (includes aria attributes). The main feature of this tag is that it displays two extra next or previous pages when dealing with the first or the last page instead of displaying just one (to manifest the marginal position of the page, i guess). It also preserves already existing url query params if there any (except for the "?page" param of course). The tag doesn't relate to pagination template object (`page_obj` by default) so it's name can be specified regardless.

## Installation
The installation is pretty simple: you just need to copy all files except for the "LICENSE" and "README.md" to a desired Django app (be careful not to overwrite some important stuff!). If you want you can manually put the template ("pagination.html") directly to your general `templates` folder for the project and put the tags' file ("pagination.py") to the `templatetags` folder of the app.

## Usage
To use this tag you need to load it first in your template:
```
{% load pagintaion %}
```
Then you need to call it and pass the number of the current page and the total number of pages (can be accessed via `page_obj`):
```
{% create_pagination current_page_number=page_obj.number pages_count=page_obj.paginator.num_pages %}
```
That will create a `<nav>` element on the page containing the pagination links. If there is only one page there will be created no pagination elements but there will be placed one `div` that takes a little bit of space to compensate the absence of it. 
