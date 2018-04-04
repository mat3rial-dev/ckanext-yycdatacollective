# ckanext-yycdatacollective
CKAN extension for YYC Data Collective

```setup.py``` is the setup script for your project. You use this script to install your project into a virtual environment. It contains several settings that you'll update as you develop your project.

```ckanext/yycdatacollective``` is the Python package directory where we'll add the source code files for our extension.

# Installation
When you install CKAN, you create a Python virtual environment in a directory on your system (```/usr/lib/ckan/default``` by default) and install the CKAN Python package and the other packages that CKAN depends on into this virtual environment. 

Before we can use our plugin, we must install our extension into our CKAN virtual environment.

Make sure your virtualenv is activated, change to the extension's directory, and run python setup.py develop:

```
. /usr/lib/ckan/default/bin/activate
cd /usr/lib/ckan/default/src/ckanext-iauthfunctions
python setup.py develop
```