<img src="https://raw.githubusercontent.com/exinmusic/new-leaf-menu/master/nlm/menu/static/img/nlm_logo.png" alt="nlm logo" width="150" height="150">

# New Leaf Menu 
This project is a live menu for dispensaries. It's meant to run on a raspberry pi in "kiosk mode", but can be served to/from anything.
The menu is populated based on a leafy menu and can be maintained that way.
If employees need to assign/reassign strains, the dashboard can be accessed from any computer on the network.
"Staff Picks" and "High CBD" flags can be assign from the dash as well.
Django admin has access to the strains model, and manipulate the table in case of dev and debugging.

## Dashboard
<img src="https://raw.githubusercontent.com/exinmusic/new-leaf-menu/master/nlm/menu/static/img/screenshot_dash.jpg">
Strains on the "no phenotype" list couldn't be assigned a phenotype from leafly and require manual assignment from the dashboard. In the example above, the dispensary uses a strain entry on leafy to advertise their prices include tax. In most cases you dont want anything on the "no phenotype" list unless it's a case like above where one of the entries is not a strain.

Along with being able to reassign strains, "Flags" can be assigned on the menu. Things like "High CBD" and "Staff Picks" and be denoted on the menu as flags.