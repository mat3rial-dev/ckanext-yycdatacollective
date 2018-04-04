# encoding: utf-8

import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

def group_create(context, data_dict=None):

	# Get the user name of the logged-in user
	user_name = context['user']

	# Get a list of the members of the 'curators' group.
	members = toolkit.get_action('member_list')(
		data_dict={'id': 'curators', 'object_type': 'user'})

    # 'members' is a list of (user_id, object_type, capacity) tuples, we're
    # only interested in the user_ids.	
    member_ids = [member_tuple[0] for member_tuple in members]

    # We have the logged-in user's user name, get their user id.
    convert_user_name_or_id_to_id = toolkit.get_converter(
    	'convert_user_name_or_id_to_id')
    user_id = convert_user_name_or_id_to_id(user_name, context)

    # Finally, we can test whether the user is a member of the curators group.
    if user_id in member_ids:
    	return {'success': True}
    else:
    	return {'success': False,
    			'msg': 'Only curators are allowed to create groups'}

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