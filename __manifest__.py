{
    "name": "HR Non-Hirable / Blacklist",
    "version": "17.0.1.0.0",
    "summary": "Mark employees as non-hirable during departure",
    "category": "Human Resources",
    "author": "Kzk",
    "license": "LGPL-3",
    "depends": [
        "base",
        "hr",
        "report",
        "hr_contract"
    ],
    "data": [
        "security/ir.model.access.csv",
        "data/demo_data.xml",
        "views/hr_non_hirable_reason_views.xml",
        "reports/hr_non_hirable_report.xml",
        "views/hr_employee_views.xml",
        "views/hr_departure_wizard_views.xml",
        "views/hr_non_hirable_menu.xml"
    ],
    "installable": true,
    "auto_install": false,
    "application": false
}