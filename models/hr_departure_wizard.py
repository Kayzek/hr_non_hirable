from odoo import api, fields, models


class HrDepartureWizard(models.TransientModel):
    _inherit = "hr.departure.wizard"

    mark_non_hirable = fields.Boolean(
        string="Mark as Non-Hirable",
        default=False,
        help="Flag this employee as non-hirable to prevent future re-hiring.",
    )
    non_hirable_reason_id = fields.Many2one(
        comodel_name="hr.non.hirable.reason",
        string="Non-Hirable Reason",
    )

    @api.onchange("mark_non_hirable")
    def _onchange_mark_non_hirable(self):
        if not self.mark_non_hirable:
            self.non_hirable_reason_id = False

    def action_register_departure(self):
        res = super().action_register_departure()
        if self.mark_non_hirable:
            self.employee_id.write({
                "is_non_hirable": True,
                "non_hirable_reason_id": self.non_hirable_reason_id.id if self.non_hirable_reason_id else False,
                "non_hirable_date": fields.Date.context_today(self),
                "non_hirable_user_id": self.env.user.id,
            })
        return res
