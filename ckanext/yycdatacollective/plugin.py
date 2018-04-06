# encoding: utf-8

'''plugin.py

'''
import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from pylons import tmpl_context as c
import ckan.lib.helpers as h

def dataset_data_retriever(dataset_data_dict):
    '''Retrieve author and mantainer name and email, as well as dataset URL.'''

    ''' Return dictionary with author and maintainer data as well as dataset URL.'''
#    contact_form_data={'pkg.maintainer': pkg.maintainer, \
#                        'pkg.maintainer_email': pkg.maintainer_email, \
#                        'pkg.author': pkg.author, \
#                        'pkg.author_email': pkg.author_email, \
#                        'pkg.dataset_url': pkg.resources[0].url
#                        }
#    print contact_form_data
#    return contact_form_data
#    print "Dataset data retriever from plugin "
#    print dataset_data_dict
#    print "DDR"

    return c


class YycdatacollectivePlugin(plugins.SingletonPlugin):
    '''An example theme plugin.

    '''
    # Declare that this class implements IConfigurer.
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IRoutes, inherit=True)

    # Declare that this plugin will implement ITemplateHelpers.
    plugins.implements(plugins.ITemplateHelpers)

    def update_config(self, config):

        # Add this plugin's templates dir to CKAN's extra_template_paths, so
        # that CKAN will use this plugin's custom templates.
        # 'templates' is the path to the templates dir, relative to this
        # plugin.py file.
        # This tells CKAN to look for template files in
        # ckanext-yycdatacollective/ckanext/yycdatacollective/templates whenever it
        # renders a page.
        toolkit.add_template_directory(config, 'templates')

    def before_map(self, map):
        map.connect('contact-us', '/contact-us',
            controller='ckanext.yycdatacollective.controller:ContactUsController',
            action='index')
        return map

    def get_helpers(self):
        '''Register the dataset_data_retriever() function above as a template
        helper function.

        '''
        # Template helper function names should begin with the name of the
        # extension they belong to, to avoid clashing with functions from
        # other extensions.
        return {'dataset_data_retriever': dataset_data_retriever}

