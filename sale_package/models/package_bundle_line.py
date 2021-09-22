from odoo import api, fields, models


class PackageBundleLine(models.Model):
    _name = "package.bundle.line"
    product_id = fields.Many2one('product.product', string="Product")
    quantity = fields.Integer(string="Quantity")
    package_id = fields.Many2one('sale.package', string="Packages")
    name = fields.Char(string="Name")
    width = fields.Integer(string="Width")
    height = fields.Integer(string="Height")
    length = fields.Integer(string="Length")
    maximum_weight = fields.Integer(string="Maximum Weight")
    pac_id = fields.Many2one('package.bundle', string='Pac')




