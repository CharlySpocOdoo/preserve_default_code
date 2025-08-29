from odoo import models

class ProductTemplate(models.Model):
    _inherit = 'product.template'
    
    def _create_variant_ids(self):
        """Preservar default_code al crear variantes"""
        original_code = self.default_code
        result = super()._create_variant_ids()
        if original_code and not self.default_code:
            self.default_code = original_code
        return result
    
    def write(self, vals):
        """Interceptar cualquier escritura que pueda borrar default_code"""
        # Guardar código antes de cualquier operación
        original_codes = {}
        for record in self:
            if record.default_code:
                original_codes[record.id] = record.default_code
        
        # Ejecutar operación original
        result = super().write(vals)
        
        # Restaurar códigos que se hayan borrado
        for record in self:
            if (record.id in original_codes and 
                original_codes[record.id] and 
                not record.default_code):
                record.default_code = original_codes[record.id]
        
        return result