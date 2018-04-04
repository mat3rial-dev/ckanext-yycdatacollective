# encoding: utf-8

import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

def group_create(context, data_dict=None):
	return {'success': False, 'msg': 'No one is allowed to create groups'}

class YycdatacollectivePlugin(plugins.SingletonPlugin):
    # plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IAuthFunctions)
    # IConfigurer

    # def update_config(self, config_):
    #     toolkit.add_template_directory(config_, 'templates')
    #     toolkit.add_public_directory(config_, 'public')
    #     toolkit.add_resource('fanstatic', 'yycdatacollective')

    def get_auth_functions(self):
        return {'group_create': group_create}        