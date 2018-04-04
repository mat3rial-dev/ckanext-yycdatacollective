# encoding: utf-8

'''plugin.py

'''
import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


class YycdatacollectivePlugin(plugins.SingletonPlugin):
    '''An example theme plugin.

    '''
    # Declare that this class implements IConfigurer.
    plugins.implements(plugins.IConfigurer)

    def update_config(self, config):

        # Add this plugin's templates dir to CKAN's extra_template_paths, so
        # that CKAN will use this plugin's custom templates.
        # 'templates' is the path to the templates dir, relative to this
        # plugin.py file.
        # This tells CKAN to look for template files in 
        # ckanext-yycdatacollective/ckanext/yycdatacollective/templates whenever it 
        # renders a page.
        toolkit.add_template_directory(config, 'templates')
