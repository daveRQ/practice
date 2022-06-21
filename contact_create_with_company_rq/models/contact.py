from odoo import models, fields, api
from odoo.exceptions import ValidationError
import json


class ResPartnerCreateWithCompany(models.Model):
    _inherit = 'res.partner'

    @api.model_create_multi
    def create(self, vals):
        res = super(ResPartnerCreateWithCompany, self).create(vals)
        return res

    @api.model
    def default_get(self, fields):
        res = super(ResPartnerCreateWithCompany, self).default_get(fields)
        # res['company_id'] = self.env.company.id
        raise ValidationError(self.env.context.get('company_id'))
        return res


