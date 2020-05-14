# -*- coding: utf-8 -*-

{
    'name' : 'Estarbien Thani - Odoo',
    'version' : '1.0.0',
    'author' : 'MSTECH',
    'category' : 'Technical Configuration',
    'summary': 'Estarbien Thani - Odoo',
    'description' : """
Módulo de personalización de Estarbien Thani en Odoo
    """,
    'website': 'http://www.mstech.pe',
    'depends' : ['payment_payulatam','auth_signup','website_calendar'],
    'data': [
        'views/auth_signup_login_templates.xml',
        'views/website_calendar_templates.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
    'sequence': 1,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
