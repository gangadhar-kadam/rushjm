from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Gymnasium"),
			"items": [
				{
					"type": "doctype",
					"name": "Customer Assesment",
					"description": _("Customer Assesment.")
				},
				{
					"type": "doctype",
					"name": "Member Details",
					"description": _("Member Details.")
				},
				{
					"type": "doctype",
					"name": "Membership Package Details",
					"description": _("Membership Package Details")
				},
				{
					"type": "doctype",
					"name": "Package Log",
					"description": _("Package Log")
				},
			]
		},
		{
			"label": _("Setup"),
			"items": [
				{
					"type": "doctype",
					"name": "Measurements",
					"description": _("Measurements.")
				},
				{
					"type": "doctype",
					"name": "Exercise Master",
					"description": _("Exercise Master.")
				},
				{
					"type": "doctype",
					"name": "Diet Master",
					"description": _("Diet Master.")
				},
				{
					"type": "doctype",
					"name": "Gymnasium Settings",
					"description": _("Gymnasium Settings")
				},
			]
		}
	]
