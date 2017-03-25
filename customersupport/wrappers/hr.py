import requests_mock
import requests
import json
import urllib.parse
from config import HR_URL
from customersupport.models import Employee
from customersupport.wrappers import mocked_responses


def get_employee(employee_id, mock=False):
    """Get the employee with the given ID."""
    get_employee_url = HR_URL + "/employees?employee_id={employee_id}".format(employee_id=employee_id)

    if mock:
        with requests_mock.Mocker() as m:
            m.get(get_employee_url, text=mocked_responses.hr_get_employee)
            r = requests.get(get_employee_url)
    else:
        r = requests.get(get_employee_url)

    json_resp = r.json()
    if "employee_array" not in json_resp:
        return None

    num_employees = len(json_resp["employee_array"])
    if num_employees > 1:
        print('The system returned multiple employees.')
        return None
    elif num_employees <= 0:
        print('No employee returned.')
        return None

    employee_resp = json_resp["employee_array"][0]
    # print(employee_resp)
    employee = Employee(employee_resp)

    return employee
