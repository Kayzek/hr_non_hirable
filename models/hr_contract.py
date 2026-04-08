from odoo import api, models, _
from odoo.exceptions import ValidationError


class HrContract(models.Model):
    _inherit = "hr.contract"

    @api.constrains("employee_id")
    def _check_employee_not_blacklisted(self):
        """Block contract creation if the employee is non-hirable."""
        for contract in self:
            if contract.employee_id and contract.employee_id.is_non_hirable:
                reason = contract.employee_id.non_hirable_reason_id.name or _("No reason provided")
                raise ValidationError(
                    _(
                        "Cannot create a contract for %s.\n"
                        "This employee is flagged as non-hirable.\n"
                        "Reason: %s"
                    ) % (
                        contract.employee_id.name,
                        reason,
                    )
                )

    @api.onchange("employee_id")
    def _onchange_employee_non_hirable_warning(self):
        if self.employee_id and self.employee_id.is_non_hirable:
            reason = self.employee_id.non_hirable_reason_id.name or _("No reason provided")
            return {
                "warning": {
                    "title": _("Non-Hirable Employee"),
                    "message": _(
                        "%s is flagged as non-hirable.\nReason: %s"
                    ) % (
                        self.employee_id.name,
                        reason,
                    ),
                }
            }
