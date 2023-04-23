# -*- coding: utf-8 -*-

{
    'name': 'vnsoft_datepicker',
    'version': '0.1',
    'category': 'hide',
    'sequence': 20,
    'summary': 'Add calendar selection plug-in function, you can limit the date selection range.',
    'description': """
Add calendar selection plug-in function, you can limit the date selection range
==========================================

    """,
    'author': 'VnSoft',
    'website': 'https://www.odoo.com/page/crm',
    # 'images': ['images/Sale_order_line_to_invoice.jpeg','images/sale_order.jpeg','images/sales_analysis.jpeg'],
    'depends': ['web'],
    'data': ["datepicker.xml"],
    "qweb":[],
    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': False,
    'application': False,
    'price': 1.99,
    'currency': 'EUR'
}
