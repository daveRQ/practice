from odoo import models, fields, api
from odoo.exceptions import ValidationError
import json


class ResPartnerCreateWithCompany(models.Model):
    _inherit = 'res.partner'

    @api.model
    def default_get(self, fields):
        res = super(ResPartnerCreateWithCompany, self).default_get(fields)
        res['company_id'] = self.env.company.id
        return res

    @api.onchange('company_id')
    def _onchange_company_id(self):
        if self.env.user not in self.env['res.groups'].search([ ('name', '=', 'Ver Compañia en Contacto') ]).users:
            raise ValidationError('No puede cambiar la Compañia')
