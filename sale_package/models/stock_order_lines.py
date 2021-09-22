from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = "stock.move"
    delivery_id = fields.Many2one('sale.order', string="Delivery")
