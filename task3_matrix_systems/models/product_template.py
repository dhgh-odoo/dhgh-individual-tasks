from odoo import models, fields, api

product_groups = [
        ('01', 'Type 1'),
        ('02', 'Type 2'),
        ('03', 'Type 3'),
        ('04', 'Type 4'),
        ('05', 'Type 5'),
        ('06', 'Type 6')]

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    product_group = fields.Selection(product_groups, string = 'Product Group', required = True, default = '01')    
    barcode = fields.Char('Barcode', compute='_compute_barcode', inverse='_set_barcode', search='_search_barcode', store=True)
    
    @api.depends('product_variant_ids.barcode','product_group')
    def _compute_barcode(self):
        '''
        Overiding the existing implementation to set the barcode based on the first two digits of the Product
        Group and the sequence number
        Format: PG.DDDDDD, PG-Product Group, D-Digit
        
        :param self-set of records associated to the context where this function is being called
        '''
        # Values for the barcode format
        sequence_size = 6
        sequence_start_position = 3
        product_group_size = 2

        for template in self:
            product_group_digits = template.product_group[:product_group_size]
            sequence_number = ""
            
            # If barcode is already set, instead of taking the next sequence number, re use the exisitng sequence            
            if template.barcode and len(template.barcode)>sequence_start_position and template.barcode[sequence_start_position:].isnumeric():
                sequence_number = self._update_barcode_all_formats(template.barcode, sequence_start_position, sequence_size)
            else:
                sequence_number = self.env['ir.sequence'].next_by_code('product.group.sequence') 
                
            template.barcode = f"{product_group_digits}.{sequence_number}"

    def _update_barcode_all_formats(self, barcode, sequence_start_position, sequence_size):
        '''
        Function to include checks if an exisiting barcode does not have the format which we have added through
        this implementation
        '''
        # Ignore the first three chars since they can be the product group and dot
        sequence_number = barcode[sequence_start_position:]

        if len(sequence_number)<sequence_size:
            sequence_number = sequence_number.rjust(sequence_size, '0')
        elif len(sequence_number)>sequence_size:
            sequence_number = sequence_number[:sequence_size]
        return sequence_number
