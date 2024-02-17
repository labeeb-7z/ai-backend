import vanna
from vanna.remote import VannaDefault


vn = VannaDefault(model='thelook', api_key='9b808b7dda444331939667cf888a8856')
vn.connect_to_...() # Connect to your database here

from vanna.flask import VannaFlaskApp
VannaFlaskApp(vn).run()