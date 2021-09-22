# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Sale Package',
    'version': '1.0',
    'summary': 'Sales Package',
    'sequence': 10,
    'description': """
    Sales Package
    """,
    'category': 'Productivity',
    'depends': ['base', 'sale', 'product', 'purchase'],
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'data/sequence.xml',
        'views/package.xml',
        'views/sale_order_package.xml',
        'views/package_info.xml',
        'views/sale_order_line_package.xml',
        'views/package_bundle.xml',
        'views/package_bundle_line.xml',
        'views/purchase_tree.xml',
        'views/purchase_tree_view.xml',
        'views/delivery_lines.xml'
        ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
