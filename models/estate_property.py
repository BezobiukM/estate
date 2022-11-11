from odoo import fields, models
from dateutil.relativedelta import relativedelta

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "estate property model"

    name = fields.Char('Title', required=True)
    description = fields.Text('Property Type')
    postcode = fields.Char('Postcode')
    date_availability = fields.Date('Date Availability', 
        default=(lambda self: (fields.Datetime.now()+relativedelta(months=3)) ), copy=False)
    expected_price = fields.Float('Expected Price', required=True)
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

    

