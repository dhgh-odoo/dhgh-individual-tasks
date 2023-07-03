{
    'name': 'matrix_systems_product_barcode',
    'description': 'Implementation for the task: "Matrix Systems : Sequential Number for Barcode"',
    'summary': 'Create a new field called Product Group which suto increments',
    'author': 'Odoo Inc.',
    'website': 'www.odoo.com',
    'sequence': 315,
    'version': '1.0',
    'application': False,
    'depends': ['product'],
    'data': [
        'data/ir_sequence_data.xml',
        'views/product_template_views_inherit.xml',
    ],
    'license': 'OPL-1',
}
