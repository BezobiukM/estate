{
    'name': 'Real Estate',
    'version': '1.0',
    'depends': ['base'],
    'author': 'Bezobiuk M',
    'category': 'Real Estate/Brokerage',
    'description': """
    Description text
    Real estate app 
    :)
    """,
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_view.xml',
        'views/estate_property_offer.xml',
        'views/estate_property_tag_view.xml',
        'views/estate_property_type_view.xml',
        'views/res_users_views.xml',
        'views/res_partner_views.xml',
        'views/estate_menus.xml'
        ]
}