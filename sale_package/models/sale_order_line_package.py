from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order.line"
    package_id = fields.Many2one('sale.package', string='Packages')
    # delivery_ids = fields.One2many('delivery.lines', "delivery_line_id",
    #                                string="Delivery")

