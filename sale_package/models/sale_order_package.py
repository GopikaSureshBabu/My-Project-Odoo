from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"
    package_ids = fields.Many2many('sale.package', string="Package")
    sale_package_ids = fields.One2many('sale.package', "pack_id",
                                       string="Sale Package")
    package_id = fields.Many2one('sale.package', string='Packages')
    package_count = fields.Integer(compute='compute_package_count')
    # delivery_ids = fields.One2many('stock.picking', 'delivery_line_id',
    #                                string="Delivery")
    sale_delivery_lines_ids = fields.One2many('stock.move', 'delivery_id',
                                              string="Delivery", copy="True")

    @api.onchange('package_ids')
    def onchange_packs_id(self):
        for rec in self:
            lines = [(5, 0)]
        for i in self.package_ids:
            val = {
                'name': i.name,
                'width': i.width,
                'height': i.height,
                'length': i.length,
                'maximum_weight': i.maximum_weight,
            }
            lines.append([0, 0, val])
        rec.sale_package_ids = lines

    def action_open_packages(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'bundle',
            'view_mode': 'tree,form',
            'res_model': 'package.bundle',
            'domain': [('sale_order_reference', '=', self.name)],
            'target': 'current',
        }

    def action_confirm(self):
        super(SaleOrder, self).action_confirm()
        line = []
        for rec in self.order_line:
            val = {
                'product_id': rec.product_id.id,
                'quantity': rec.product_uom_qty,
                'name': rec.package_id.name,
                'width': rec.package_id.width,
                'height': rec.package_id.height,
                'length': rec.package_id.length,
                'maximum_weight': rec.package_id.maximum_weight,
            }
            line.append((0, 0, val))
        vals = {
            'partner_id': self.partner_id.id,
            'sale_order_reference': self.name,
            'date': self.date_order,
            'expected_date': self.commitment_date,
            'line_ids': line
        }
        self.env['package.bundle'].sudo().create(vals)

    def action_confirm(self):
        super(SaleOrder, self).action_confirm()
        print(self.sale_delivery_lines_ids)
        for rec in self.sale_delivery_lines_ids:
            self.env['stock.move'].create(
                {
                     'product.id': rec.product_id,
                }
            )
            
        # return{
        #     'type': 'ir.actions.act_window',
        #     'name': 'Delivery Lines',
        #     'view_mode': 'tree,form',
        #     'res_model': 'stock.move',
        #     'target': 'current',
        # }



        # for rec in self.order_line:
        #     val = {
        #         'product_id': rec.product_id.id,
        #         'quantity': rec.product_uom_qty,
        #         'name': rec.package_id.name,
        #         'width': rec.package_id.width,
        #         'height': rec.package_id.height,
        #         'length': rec.package_id.length,
        #         'maximum_weight': rec.package_id.maximum_weight,
        #     }
        #     line.append((0, 0, val))
        # vals = {
        #     'partner_id': self.partner_id.id,
        #     'sale_order_reference': self.name,
        #     'date': self.date_order,
        #     'expected_date': self.commitment_date,
        #     'line_ids': line
        # }
        # self.env['package.bundle'].sudo().create(vals)

    def compute_package_count(self):
        for record in self:
            record.package_count = self.env['package.bundle'].search_count(
                [('sale_order_reference', '=', self.name)])
