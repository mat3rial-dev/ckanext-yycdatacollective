# encoding: utf-8

'''plugin.py

'''
import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from pylons import tmpl_context as c
import ckan.lib.helpers as h
import ast


def dataset_data_retriever(context, dataset_data_dict):
    '''Retrieve author and mantainer name and email, as well as dataset URL.'''

    ''' Return dictionary with author and maintainer data as well as dataset URL.'''

#    print dataset_data_dict
#    print "END"
#    print "PLUGIN-Context: {0}\n".format(context.data_dict)

    contact_form_data=dict(context.data_dict)
    if contact_form_data:
        # print "contact_form_data:{0}".format(contact_form_data)
        contact_form_data = ast.literal_eval(contact_form_data['dataset_data_dict'])
        contact_form_data['request_ip']=context.remote_addr
        # print "contact_form_data_2:{0}".format(contact_form_data)

    return contact_form_data


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
        map.connect('contact-us', '/dataset/{id}/us',
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

