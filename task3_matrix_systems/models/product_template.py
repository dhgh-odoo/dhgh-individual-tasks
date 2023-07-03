from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    product_group = fields.Selection([
        ('00', 'Type 1'),
        ('01', 'Type 2'),
        ('03', 'Type 3'),
        ('04', 'Type 4'),
        ('05', 'Type 5'),
        ('06', 'Type 6')],
        string = 'Product Group',
        required = True,
        default = '00')    
    barcode = fields.Char('Barcode', compute='_compute_barcode', inverse='_set_barcode', search='_search_barcode', store=True)
    
    @api.depends('product_variant_ids.barcode','product_group')
    def _compute_barcode(self):
        '''
        Overiding the existing implementation to set the barcode based on the first two digits of the Product
        Group and the sequence number
        :param self-set of records associated to the context where this function is being called
        '''
        for template in self:
            product_group_digits = template.product_group[:2]
            sequence_number = ""
            
            if not template.barcode:
                sequence_number = self.env['ir.sequence'].next_by_code('product.group.sequence')
            else: 
                sequence_number = template.barcode[3:]
                
            template.barcode = product_group_digits + "." + sequence_number
