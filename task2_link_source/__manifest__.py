{
    'name': 'LinkSource_sale',
    'description': 'Implementation for the task: "LinkSource Pricing Update"',
    'summary': 'Removed the Auto Updation of Unit Price when you update the quantity',
    'author': 'Odoo Inc.',
    'website': 'www.odoo.com',
    'sequence': 315,
    'version': '1.1',
    'application': False,
    'depends': ['sale'],
    'data': [
        'views/sale_order_inherit.xml'
    ],
    'license': 'OPL-1',
}
