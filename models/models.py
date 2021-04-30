# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Contrato(models.Model):
    _inherit = 'contract.contract'
    _description = 'model.technical.name'
    
    pago_anual = fields.Boolean(string='Pago Anual')
    fecha_inicio = fields.Date(string='Fecha Inicio Contrato')
    contract_total = fields.Float(string='Total del Contrato')
    
    @api.onchange('contract_line_ids','contract_line_ids.quantity','contract_line_ids.price_unit')
    def _onchange_contract_total(self):
        total=0
        for i in self.contract_line_ids:
            total+=i.price_subtotal
        self.contract_total=total

