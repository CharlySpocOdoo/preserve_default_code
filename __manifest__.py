{
    'name': 'Preserve Product Reference',
    'version': '18.0',  # Ajusta según tu versión de Odoo
    'summary': 'Preserve product template reference when creating variants',
    'description': """
        This module prevents the default_code field from being cleared
        when creating product variants.
    """,
    'author': 'Charly boy',
    'website': 'https://rosadelimma.mx',
    'category': 'Product',
    'depends': ['product'],
    'data': [],
    'installable': True,
    'auto_install': False,
    'application': False,
}