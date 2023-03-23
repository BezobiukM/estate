{
    'name': 'Real Estate',
    'version': '1.0',
    'depends': ['base', 'web'],
    'author': 'Maria Bezobiuk',
    'category': 'Real Estate/Brokerage',
    'description': """
    The Real Estate Advertisement module. 
    Helps you manage your real estate.
    To load demo data create a new DB with checked Demo Data and install the app.
    """,
    'data': [
        'security/estate_security.xml',
        'security/ir.model.access.csv',
        'data/res_partner_data.xml',
        'views/estate_property_view.xml',
        'views/estate_property_offer.xml',
        'views/estate_property_tag_view.xml',
        'views/estate_property_type_view.xml',
        # 'data/estate_property_type_data.xml',
        'views/res_users_views.xml',
        'views/res_partner_views.xml',
        'views/estate_menus.xml',
        'report/estate_property_templates.xml',
        'report/estate_property_reports.xml',
        'data/estate_demo.xml',
    ],
    'demo': [
        'demo/res_partner_demo.xml',
        'demo/res_company_demo.xml',
        'demo/res_users_demo.xml',
        'demo/estate_property_demo.xml',
        'demo/estate_property_offer_demo.xml'
    ],
    'assets': {
        'web.assets_backend': [
           'estate/static/src/js/tree_button.js',
        ],
        'web.assets_qweb': [
            'estate/static/src/xml/tree_button.xml',
        ]
    },
    'installable': True,
    'application': True,
    'auto_install': False
}
