from odoo import fields, models
from dateutil.relativedelta import relativedelta

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "estate property model"

    name = fields.Char('Title', required=True)
    tag_ids = fields.Many2many('estate.property.tag', string='Tags')
    property_type_id = fields.Many2one('estate.property.type', string='Property Type')
    expected_price = fields.Float('Expected Price', required=True)
    postcode = fields.Char('Postcode')
    best_price = fields.Float('Best Offer', 
        readonly=True, copy=False)
    date_availability = fields.Date('Available From', 
        default=(lambda self: (fields.Datetime.now()+relativedelta(months=3)) ), copy=False)
    selling_price = fields.Float('Selling Price', 
        readonly=True, copy=False)
    
    active = fields.Boolean()
    state = fields.Selection(
        selection=[
            ('new', 'New'),
            ('offer_received', 'Offer Received'),
            ('offer_accepted', 'Offer Accepted'),
            ('sold', 'Sold'),
            ('canceled', 'Canceled')],
         required=True, copy=False, default='new'
    )
    bedrooms = fields.Integer('Bedrooms', default=2)
    living_area = fields.Integer('Living Area (sqm)', required=True)
    facades = fields.Integer('Facades')
    garage = fields.Boolean('Garage')
    garden = fields.Boolean('Garden')
    garden_area = fields.Integer('Garden Area')
    garden_orientation = fields.Selection(
        string = 'Garden Orientation',
        selection = [('north', 'North'), ('South', 'South'),
        ('east', 'East'), ('west', 'West')
        ])

    salesman = fields.Many2one('res.users', string='Salesman', required=True, default=lambda self: self.env.user)
    buyer = fields.Many2one('res.partner', string='Buyer', required=True)
    description = fields.Text('Description')

    offer_ids = fields.One2many('estate.property.offer', 'property_id', string='Offer')

    

