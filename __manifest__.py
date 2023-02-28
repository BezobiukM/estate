{
    'name': 'Real Estate',
    'version': '1.0',
    'depends': ['base'],
    'author': 'Maria Bezobiuk',
    'category': 'Real Estate/Brokerage',
    'description': """
    The Real Estate Advertisement module. 
    Helps you manage your real estate.
    """,
    'data': [
        'security/estate_security.xml',
        'security/ir.model.access.csv',
        'views/estate_property_view.xml',
        'views/estate_property_offer.xml',
        'views/estate_property_tag_view.xml',
        'views/estate_property_type_view.xml',
        'views/res_users_views.xml',
        'views/res_partner_views.xml',
        'views/estate_menus.xml',
        'report/estate_property_templates.xml',
        'report/estate_property_reports.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}
