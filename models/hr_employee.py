from odoo import api, fields, models


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    is_non_hirable = fields.Boolean(
        string="Non-Hirable",
        default=False,
        tracking=True,
        help="When enabled, this employee is flagged as non-hirable.",
    )
    non_hirable_reason_id = fields.Many2one(
        comodel_name="hr.non.hirable.reason",
        string="Non-Hirable Reason",
        tracking=True,
    )
    non_hirable_date = fields.Date(
        string="Blacklist Date",
        readonly=True,
    )
    non_hirable_user_id = fields.Many2one(
        comodel_name="res.users",
        string="Blacklisted By",
        readonly=True,
    )

    def action_toggle_non_hirable(self):
        """Toggle the non-hirable flag with audit trail."""
        for employee in self:
            if employee.is_non_hirable:
                employee.write({
                    "is_non_hirable": False,
                    "non_hirable_reason_id": False,
                    "non_hirable_date": False,
                    "non_hirable_user_id": False,
                })
            else:
                employee.write({
                    "is_non_hirable": True,
                    "non_hirable_date": fields.Date.context_today(employee),
                    "non_hirable_user_id": self.env.user.id,
                })
