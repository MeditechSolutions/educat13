# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning

class PaymentAcquirerPayulatam(models.Model) :
    _inherit = 'payment.acquirer'
    
    def payulatam_form_generate_values(self, values) :
        payulatam_values = super(PaymentAcquirerPayulatam, self).payulatam_form_generate_values(values)
        if self.payulatam_account_id == '512323' and self.state == 'test' :
            payulatam_values['currency'] = 'ARS'
            payulatam_values['signature'] = self._payulatam_generate_sign("in", payulatam_values)
        return payulatam_values
