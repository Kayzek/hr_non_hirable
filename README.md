# HR Non-Hirable / Blacklist

## Overview
**HR Non-Hirable / Blacklist** is an Odoo 17 module that extends the standard Human Resources functionality to allow marking employees as "non-hirable" or "blacklisted" during their departure process. It helps organizations keep track of former employees who should not be re-hired in the future.

## Features
* **Non-hirable Flag:** Adds a capability on employee profiles to mark them as non-hirable.
* **Reason Tracking:** Allows specifying custom reasons for marking an employee as non-hirable.
* **Departure Wizard Integration:** Integrates seamlessly with Odoo's standard departure wizard, enabling you to mark the employee as non-hirable at the moment of departure.

## Dependencies
This module depends on the following standard Odoo modules:
* `hr` (Employees)
* `hr_contract` (Employee Contracts)

## Installation
1. Place the `hr_non_hirable` directory into your Odoo addons path.
2. Restart the Odoo server.
3. Update the app list in Odoo with Developer Mode enabled.
4. Search for "HR Non-Hirable / Blacklist" and install the module.

## Usage
1. Provide reasons for non-hirability under the new settings or menus (often added under **Employees -> Configuration -> Non-Hirable Reasons**).
2. When an employee leaves, use the standard **Register Departure** wizard. You will find an option to mark them as non-hirable and specify a reason.
3. Employee profiles will show their non-hirable status and the related reason, preventing accidental re-hiring.

## Author
* **Kzk**

## License
This module is licensed under the LGPL-3.0 License.
