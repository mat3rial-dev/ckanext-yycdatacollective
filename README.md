# ckanext-yycdatacollective
CKAN extension for YYC Data Collective

```setup.py``` is the setup script for your project. You use this script to install your project into a virtual environment. It contains several settings that you'll update as you develop your project.

```ckanext/yycdatacollective``` is the Python package directory where we'll add the source code files for our extension.

The ```context``` parameter is a dictionary that CKAN passes to all authorization and action functions containing some computed variables. 

The ```data_dict``` parameter is another dictionary that CKAN passes to all authorization and action functions. ```data_dict``` contains any data posted by the user to CKAN.

# Installation
When you install CKAN, you create a Python virtual environment in a directory on your system (```/usr/lib/ckan/default``` by default) and install the CKAN Python package and the other packages that CKAN depends on into this virtual environment. 

Before we can use our plugin, we must install our extension into our CKAN virtual environment.

Make sure your virtualenv is activated, change to the extension's directory, and run python setup.py develop:

```
. /usr/lib/ckan/default/bin/activate
cd /usr/lib/ckan/default/src/ckanext-yycdatacollective
```
Install the python modules required by the extension and then install the extension

```
pip install -r requirements.txt
python setup.py develop
```

# Enabling the plugin

An extension’s plugins must be added to the ckan.plugins setting in your CKAN config file so that CKAN will call the plugins' methods. The name that you gave to your plugin class in the left-hand-side of the assignment in the ```setup.py``` file is the name you'll use for your plugin in CKAN's config file:

```
ckan.plugins = ... other plugins ... yycdatacollective
```
