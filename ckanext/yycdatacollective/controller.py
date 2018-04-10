import ckan.lib.base as base
import ckan.lib.helpers as h
import ckan.plugins as p
import ckan.plugins.toolkit as tk
from ckan.lib.base import BaseController, config
import jinja2
from ckan.common import _, c, g, request
from validate_email import validate_email
from ckan.logic import action
import ckan.model as model

c = base.c

abort = base.abort
render = base.render

class ContactUsController(BaseController):
    def index(self, context=None):
        # c = p.toolkit.c
        data = request.params or {}
        errors = {}
        error_summary = {}

        r = request.environ
        # print "request: {0}".format(r)

        user_ip = r['REMOTE_ADDR']
        dataset_id = r['wsgiorg.routing_args'][1]['id']

        # if you use get_action, the context object is automatically populated for you with the model and user keys (https://lists.okfn.org/pipermail/ckan-dev/2013-May/004878.html)
        result = p.toolkit.get_action('package_show')({}, {'id': dataset_id})

        resources = result['resources']
        # print "result: {0}".format(result)

        resource_url = [resource['url'] for resource in resources]
        resource_url_txt = '\n\n'.join(resource_url)
        # print resource_url_txt

        if not data == {}:
            import ckan.lib.mailer
            if data.get('contact_us.nochange') != 'http://':
                errors['contact_us.nochange'] = [_('The value was edited')]
            if not data.get('contact_us.name'):
                errors['contact_us.name'] = [_('Missing value')]
            if not data.get('contact_us.email'):
                errors['contact_us.email'] = [_('Missing value')]
            elif not validate_email(data.get('contact_us.email')):
                errors['contact_us.email'] = [_('Invalid email')]
            if not data.get('contact_us.message'):
                errors['contact_us.message'] = [_('Missing value')]

            if errors == {}:
                try:
                    # fetch information from YYC admin email from config
                    emails = config.get('contact_us.email')
                    for v in emails.split(','):
                        # print "V: {0}".format(v)
                        ckan.lib.mailer._mail_recipient( 
                            'Admin', 
                            v, 
                            data.get('contact_us.name'), 
                            data.get('contact_us.email'), 
                            'Contact form', 
                            data.get('contact_us.message'))
                    # public user email
                        ckan.lib.mailer._mail_recipient(
                            recipient_name=data.get('contact_us.name'),
                            recipient_email=data.get('contact_us.email'),
                            sender_name="YYC Data Collective",
                            sender_url=data.get('contact_us.name'),
                            subject="YYC Download authorization",
                            body="Dear " + data.get('contact_us.name') +
                            ",\n\nYou requested access to a restricted dataset"
                            " hosted in the YYC Data Collective website from "
                            "the IP address " + user_ip + ".\n\nYou can "
                            "download the resource(s) of that dataset through "
                            "the following link(s): \n\n" +
                            resource_url_txt + "\n\nYours,\n\nYYC Data "
                            "Collective")
                    h.flash_success(_('Email sent'))
                    data = {}
                except ckan.lib.mailer.MailerException:
                    raise

        vars = {'data': data, 'errors': errors, 'error_summary': error_summary}
        return render('ckanext/contact_us/index.html', extra_vars=vars)
