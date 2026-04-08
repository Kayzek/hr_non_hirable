from odoo import fields, models


class HrNonHirableReason(models.Model):
    _name = "hr.non.hirable.reason"
    _description = "Non-Hirable Reason Category"
    _order = "sequence, name"

    name = fields.Char(string="Reason", required=True, translate=True)
    code = fields.Char(string="Code")
    active = fields.Boolean(default=True)
    sequence = fields.Integer(default=10)
    description = fields.Text(string="Description")
    color = fields.Integer(string="Color")

    _sql_constraints = [
        ("code_unique", "UNIQUE(code)", "The code must be unique."),
    ]
