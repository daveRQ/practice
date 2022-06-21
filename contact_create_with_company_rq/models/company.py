from odoo import models, fields, api
from odoo.exceptions import ValidationError
import json


class ResCompanyStore(models.Model):
    _inherit = 'res.company'

    contact_add_company = fields.Boolean(compute='_compute_contact_add_company', string='Contact ADd Company')

    def _compute_contact_add_company(self):
        for rec in self:
            if rec.partner_id:
                rec.partner_id.company_id = rec.id
            rec.contact_add_company = True
