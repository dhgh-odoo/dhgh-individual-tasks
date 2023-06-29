from odoo import api, models
from odoo.exceptions import ValidationError

class StockMove(models.Model):
    _inherit = "stock.move"
    
    @api.onchange('product_uom_qty','quantity_done')
    def _check_quantity_done(self):
        '''
        Checks if quantity_done must be equal or less than the demand for receipts in the Invetory
        App
        :param self - set of records associated to the context where this function is being called
        '''
        for record in self:
            picking_type_record = self.env['stock.picking.type'].search([('id','=',record.picking_type_id.id)])
            
            if picking_type_record.code=="incoming" and record.quantity_done > record.product_uom_qty:
                raise ValidationError('Odoopsie! Quantity done must be less than or equal to demand')