from odoo import api, fields, models


class Product(models.Model):
    _inherit = "product.template"
    lines_ids = fields.Many2many("purchase.order", string="Lines Product")
    # reference_no = fields.Char(string="Reference NO")

    # @api.model
    # def default_get(self, field):
    #     values = super(Product, self).default_get(self, field)
    #     print(field)
    #     lines = []
    #     book_rec = self.env['purchase.order'].search([])
    #     for rec in book_rec:
    #         line = (0, 0, {'reference_no': rec.name})
    #         lines.append(line)
    #     values.update({'lines_ids': lines})
    #     # values['lines_ids':lines]
    #     return values

    # @api.model
    # def default_get(self, name, partner_id, status):
    #     res = super(Product, self).default_get(self, name, partner_id, status)

    # print(name, partner_id, status)
    # return{
    #     'type': 'ir.actions.act_window',
    #     'name': 'Purchase',
    #     'view_mode': 'tree',
    #     'res_model': 'product.template',
    #     'target': 'current',
    # }

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
