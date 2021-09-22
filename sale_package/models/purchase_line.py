from odoo import api, fields, models


class ProductPurchaseOrderLine(models.Model):
    _name = "product.purchase.order.line"
    # products_id = fields.Many2one('product.product', string='Products')
    # reference_no = fields.Char(string="Reference NO")
    # current_status = fields.Selection([('draft', 'RFQ'), ('sent', 'RFQ Sent'),
    #                                    ('to approve', 'To Approve'),
    #                                    ('purchase', 'Purchase Order'),
    #                                    ('done', 'Locked'),
    #                                    ('cancel', 'Cancelled')],
    #                                   string='Status', readonly=True)
