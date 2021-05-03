# Rest_API_Blender

Blender models Rest Api

## install :

install Django --> https://docs.djangoproject.com/fr/3.1/topics/install/

clone the git project

Give the user ownership on the entire folder.

```sudo chmod user *```

In apiblencs/settings.py set the hosts ip adress you want the server to run on or just put localhost or 127.0.0.1 for local use.

```ALLOWED_HOSTS = ['your_ip']```

Most problems encountered with the software are caused by a bad installation of Django or the user used to run the server not having ownership of the files

## how to run : 
launch the server whith the following comand:

```python manage.py runserver *ip*:*port*```

in browser open : http://*ip*:*port*/

replace *ip* and *port* with the one you intend to use,dont forget to make sure that the ports you intend to use is open on your network

## how to add Blender models : 
if you are a member of this project 
in browser open the admin panel : http://*ip*:*port*/admin/myapi/blendermodel/
and connect and you will be redirected to the page to add Blender models
if not please contact an admin to have an access to the admin panel
