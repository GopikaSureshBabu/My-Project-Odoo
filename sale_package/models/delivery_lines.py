from odoo import api, fields, models


class DeliveryLines(models.Model):
    _name = "delivery.lines"
    # delivery_line_id = fields.Many2one('sale.order',
    #                                    string="Delivery Line")
