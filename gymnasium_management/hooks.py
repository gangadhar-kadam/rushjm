# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "gymnasium_management"
app_title = "Gymnasium Management"
app_publisher = "email.kadam@gmail.com"
app_description = "Gymnasium Mgmt"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "email.kadam@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/gymnasium_management/css/gymnasium_management.css"
# app_include_js = "/assets/gymnasium_management/js/gymnasium_management.js"

# include js, css files in header of web template
# web_include_css = "/assets/gymnasium_management/css/gymnasium_management.css"
# web_include_js = "/assets/gymnasium_management/js/gymnasium_management.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "gymnasium_management.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "gymnasium_management.install.before_install"
# after_install = "gymnasium_management.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "gymnasium_management.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

fixtures = ["Web Form",'Custom Field','Property Setter']

doc_events = {
	"Sales Invoice": {
		"on_submit": "gymnasium_management.gymnasium_management.doctype.membership_package_details.membership_package_details.create_membership_package_details",
		"on_cancel": "gymnasium_management.gymnasium_management.doctype.membership_package_details.membership_package_details.cancel_si_membership_package_details"
	},
}

# Scheduled Tasks
# ---------------

scheduler_events = {
	"daily": [
		"gymnasium_management.gymnasium_management.doctype.membership_package_details.membership_package_details.create_package_log"
	]
}

# Testing
# -------

# before_tests = "gymnasium_management.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "gymnasium_management.event.get_events"
# }

