
import ckan.lib.base as base
import ckan.lib.helpers as h
import ckan.plugins as p
import ckan.plugins.toolkit as tk
from ckan.lib.base import BaseController, config
import jinja2
from ckan.common import _, c, g, request
from validate_email import validate_email
from pylons import request, config, tmpl_context as c
import ast

abort = base.abort
render = base.render

class ContactUsController(BaseController):
    def index(self, context=None):
#        c = p.toolkit.c
        data = request.params or {}
        print "DATA: {0}".format(data)
        d = ast.literal_eval(dict(data)['dataset_data_dict'])
        dataset_url = d['pkg.dataset_url']
        errors = {}
        error_summary = {}
        print config.get('email_to');

        if not data == {} :
            import ckan.lib.mailer
            if data.get('contact_us.nochange') != 'http://' :
                errors['contact_us.nochange'] = [_('The value was edited')]
            if not data.get('contact_us.name') :
                errors['contact_us.name'] = [_('Missing value')]
            if not data.get('contact_us.email') :
                errors['contact_us.email'] = [_('Missing value')]
            if not data.get('contact_us.institution') :
                errors['contact_us.institution'] = [_('Missing value')]
            elif not validate_email(data.get('contact_us.email')):
                errors['contact_us.email'] = [_('Invalid email')]
            if not data.get('contact_us.message') :
                errors['contact_us.message'] = [_('Missing value')]



            if errors == {} :
                try:
                    # fetch information from YYC admin email from config
                    emails = config.get('contact_us.email')
                    for v in emails.split(','): 
                        print "V: {0}".format(v)
                        ckan.lib.mailer._mail_recipient( \
                            'Admin', \
                            v, \
                            data.get('contact_us.name'), \
                            data.get('contact_us.email'), \
                            'Contact form', \
                            data.get('contact_us.message')
                            )
                    # public user email
                        ckan.lib.mailer._mail_recipient( \
                            recipient_name=data.get('contact_us.name'), \
                            recipient_email=data.get('contact_us.email'), \
                            sender_name="YYC Data Collective", \
                            sender_url=data.get('contact_us.name'), \
                            subject="YYC Download authorization", \
                            body=dataset_url
                            )

                    h.flash_success(_('Email sent'))
                    data = {}
                except ckan.lib.mailer.MailerException:
                    raise
        #error_summary = errors
        vars = {'data': request.params, 'errors': errors, 'error_summary': error_summary}
        # c.data_dict = data

        return render('ckanext/contact_us/index.html', extra_vars=vars)

# def _mail_recipient(recipient_name,
#                         recipient_email,
#                         sender_name, 
#                         sender_url, 
#                         subject,
#                         body,
#                         headers=None)


