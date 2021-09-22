from odoo import api, fields, models


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"
    # product_purchase_id = fields.Many2one('product.template', string='Products')
    # partner_id = fields.Many2one('res.partner', string="Partner")
    # name = fields.Char(string="Reference NO")
    # state = fields.Selection(related="purchase_order.state", string="Status")




        # line = []
        # for rec in self:
        #     value = {
        #         'partner_id': rec.partner_id,
        #         'reference_no': rec.name,
        #         'current_status': rec.state,
        #     }
        #     line.append((0, 0, value))
        # val = {
        #     'lines_ids': line
        # }
        # self.env['product.template'].write(val)

        #
        # line = []
        # for rec in self:
        #     value = {
        #         'products_id': rec.order_line.product_id,
        #         'reference_no': rec.name,
        #         'current_status': rec.state,
        #     }
        #     line.append((0, 0, value))
        # val = {
        #     'lines_ids': line
        # }
        # self.env['product.template'].create(val)


