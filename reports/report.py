from odoo import models, _
from datetime import datetime


class ReportNonHirable(models.AbstractModel):
    _name = "report.hr_non_hirable.report_non_hirable_document"
    _description = "Non-Hirable Employees Report"

    def _get_report_values(self, docids, data=None):
        employees = self.env["hr.employee"].sudo().with_context(active_test=False).search(
            [("is_non_hirable", "=", True)], order="company_id, name"
        )
        companies = employees.mapped("company_id").sorted(key=lambda c: c.name)
        datetime_now = datetime.now().strftime("%d/%m/%Y %H:%M")
        company_name = self.env.company.name
        companies_data = []
        total_count = 0

        for company in companies:
            company_employees = employees.filtered(lambda e: e.company_id.id == company.id)
            total_count += len(company_employees)
            emps_data = []
            for emp in company_employees:
                contract = emp.contract_ids.sorted(key=lambda c: c.date_start, reverse=True)[:1]
                contract_start = contract.date_start.strftime("%d/%m/%Y") if contract and contract.date_start else ""
                contract_end = contract.date_end.strftime("%d/%m/%Y") if contract and contract.date_end else _("Indefinite")
                emps_data.append({
                    "name": emp.name,
                    "identification_id": emp.identification_id or "",
                    "non_hirable_reason": emp.non_hirable_reason_id.name or "",
                    "work_location": (emp.work_location_id.name if getattr(emp, 'work_location_id', False) else "") or "",
                    "contract_start": contract_start,
                    "contract_end": contract_end,
                    "job": emp.job_id.name or "",
                    "department": emp.department_id.name or "",
                })
            companies_data.append({
                "company": company,
                "employees": emps_data,
            })

        return {
            "doc_ids": docids,
            "doc_model": "hr.employee",
            "datetime_now": datetime_now,
            "company_name": company_name,
            "companies": companies_data,
            "total_count": total_count,
            "search_placeholder": _("Search in report..."),
        }


class ReportNonHirableHtml(models.AbstractModel):
    _name = "report.hr_non_hirable.report_non_hirable_document_html"
    _description = "Non-Hirable Employees HTML Report"

    def _get_report_values(self, docids, data=None):
        return self.env["report.hr_non_hirable.report_non_hirable_document"]._get_report_values(docids, data)

