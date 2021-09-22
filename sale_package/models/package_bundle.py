from odoo import api, fields, models, _


class PackageBundle(models.Model):
    _name = "package.bundle"
    partner_id = fields.Many2one('res.partner', string="Customer")
    sequence_no = fields.Char(string="Sequence NO", required=True, copy=False,
                              readonly=True, index=True,
                              default=lambda self: _('New'))
    sale_order_reference = fields.Char(string="SO Reference")
    date = fields.Datetime(string="Date")
    expected_date = fields.Datetime(string="Expected Date")
    package_details = fields.Char(string="Package Details")
    line_ids = fields.One2many('package.bundle.line', "pac_id", string="Line")

    @api.model
    def create(self, vals):
        if vals.get('sequence_no', _('New')) == _('New'):
            vals['sequence_no'] = self.env['ir.sequence'].next_by_code(
                'package.bundle.sequence') or _('New')
        result = super(PackageBundle, self).create(vals)
        return result
