#!/usr/bin/env python3

from config import CONN, CURSOR
from department import Department

import ipdb

Department.drop_table()
Department.create_table()

payroll = Department("Payroll", "Building A, 5th Floor")
print(payroll)  # <Department None: Payroll, Building A, 5th Floor>

payroll.save()  # Persist to db, assign object id attribute
print(payroll)  # <Department 1: Payroll, Building A, 5th Floor>

hr = Department("Human Resources", "Building C, East Wing")
print(hr)  # <Department None: Human Resources, Building C, East Wing>

hr.save()  # Persist to db, assign object id attribute
print(hr)  # <Department 2: Human Resources, Building C, East Wing>

accounting = Department.create("Accounting", "Building B, 1st Floor")
print(accounting)  #  <Department 3: Accounting, Building B, 1st Floor>

accounting.name = 'Corporate Accounting'
accounting.location = "Building D, 10th Floor"
accounting.update()
print(accounting)  # <Department 3: Corporate Accounting, Building D, 10th Floor>

hr.delete()  # delete from db table, but object still exists in memory
print(hr)  # <Department 2: Human Resources, Building C, East Wing>

ipdb.set_trace()
