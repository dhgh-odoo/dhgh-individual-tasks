from odoo import models


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    # Override the function to avoid auto changing the price_unit when quantity changes
    def _get_display_price(self):
        self.ensure_one()
        if self.env.context.get('use_pricelist')==True:
            modified_record = self.with_company(self.company_id)
            return super(SaleOrderLine,modified_record)._get_display_price()
        return self.price_unit  
        