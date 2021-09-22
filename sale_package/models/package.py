from odoo import api, fields, models


class SalePackage(models.Model):
    _name = "sale.package"
    _description = "Sale Package"
    name = fields.Char(string="Name", required=True, tracking=True)
    width = fields.Integer(string="Width", tracking=True)
    height = fields.Integer(string="Height", tracking=True)
    length = fields.Integer(string="Length", tracking=True)
    maximum_weight = fields.Integer(string="Maximum Weight", tracking=True)
    pack_id = fields.Many2one('sale.order', string="Pack")


