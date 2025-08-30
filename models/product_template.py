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


class ProductProduct(models.Model):
    _inherit = 'product.product'
    
    def write(self, vals):
        """Interceptar cambios en variantes que afecten el template"""
        # Si se está modificando default_code de una variante
        if 'default_code' in vals:
            # Guardar los códigos originales de los templates padre
            template_codes = {}
            for variant in self:
                template = variant.product_tmpl_id
                if template.default_code:
                    template_codes[template.id] = template.default_code
        
        # Ejecutar operación original
        result = super().write(vals)
        
        # Restaurar códigos de templates que se hayan borrado
        if 'default_code' in vals:
            for variant in self:
                template = variant.product_tmpl_id
                if (template.id in template_codes and 
                    template_codes[template.id] and 
                    not template.default_code):
                    template.default_code = template_codes[template.id]
        
        return result