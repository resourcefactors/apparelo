# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "apparelo"
app_title = "Apparelo"
app_publisher = "Aerele Technologies Private Limited"
app_description = "Frappe application to manage the manufacturing workflows in the garment industry."
app_icon = "business-time"
app_color = "grey"
app_email = "apparelo@aerele.in"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/apparelo/css/apparelo.css"
# app_include_js = "/assets/apparelo/js/apparelo.js"

# include js, css files in header of web template
# web_include_css = "/assets/apparelo/css/apparelo.css"
# web_include_js = "/assets/apparelo/js/apparelo.js"

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
# get_website_user_home_page = "apparelo.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "apparelo.install.before_install"
after_install = "apparelo.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "apparelo.notifications.get_notification_config"

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

doc_events = {
	"Location": {
		"after_insert": "apparelo.apparelo.doctype.lot_creation.custom_scripts.create_surplus_location_warehouse"
	},
	"Supplier": {
		"after_insert": "apparelo.apparelo.doctype.lot_creation.custom_scripts.create_supplier_warehouse"
	},
	"Item": {
		"validate": "apparelo.erpnext_hooks.populate_pf_item_code"
	},
	"Purchase Order": {
		"validate": "apparelo.apparelo.doctype.lot_creation.custom_scripts.set_lot_link_field_in_po"
		}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"apparelo.tasks.all"
# 	],
# 	"daily": [
# 		"apparelo.tasks.daily"
# 	],
# 	"hourly": [
# 		"apparelo.tasks.hourly"
# 	],
# 	"weekly": [
# 		"apparelo.tasks.weekly"
# 	]
# 	"monthly": [
# 		"apparelo.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "apparelo.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "apparelo.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "apparelo.task.get_dashboard_data"
# }