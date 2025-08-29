from odoo import models

class ProductTemplate(models.Model):
    _inherit = 'product.template'
    
    def _create_variant_ids(self):
        """Sobrescribir para preservar default_code"""
        original_code = self.default_code
        result = super()._create_variant_ids()
        if original_code and not self.default_code:
            self.default_code = original_code
        return result