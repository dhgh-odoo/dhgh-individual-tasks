from odoo import fields, models, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_recompute_price_unit(self):
        """
        Action for the recompute prices button. 
        Calls the _get_display_prices() and pass to context to differrentiate using pricelist for every sales order line
        :param self - set of records associated to the context where this function is being called
        """
        for record in self:
            # Get all the sale order lines linked to this order
            order_lines = self.env['sale.order.line'].search([('order_id','=',record.id)])
            
            # Update context to trigger the _get_display_price() from SalesOrderLine instead of the overriden class 
            context = self.env.context.copy()
            context.update({'use_pricelist': True})
            
            for line in order_lines:

                price = line.with_company(line.company_id).with_context(context)._get_display_price()
                line.price_unit = line.product_id._get_tax_included_unit_price(
                    line.company_id,
                    line.order_id.currency_id,
                    line.order_id.date_order,
                    'sale',
                    fiscal_position=line.order_id.fiscal_position_id,
                    product_price_unit=price,
                    product_currency=line.currency_id)

