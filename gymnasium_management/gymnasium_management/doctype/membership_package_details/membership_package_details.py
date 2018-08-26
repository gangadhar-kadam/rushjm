# -*- coding: utf-8 -*-
# Copyright (c) 2018, email.kadam@gmail.com and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils import cint, today, add_days
from frappe import msgprint, _

class MembershipPackageDetails(Document):
	pass



def create_membership_package_details(doc, method):
	if cint(doc.is_return)==1:
		for item in doc.items:
			mmpd_name= frappe.db.get_value("Membership Package Details",{"sales_invoice":doc.return_against,"package_name":item.item_code},"name")
			if mmpd_name:
				try:
					mpd_obj = frappe.get_doc("Membership Package Details",mmpd_name)
					mpd_obj.disabled=1
					mpd_obj.flags.ignore_permissions = 1
					mpd_obj.save()
				except Exception as e:
					msgprint(_("Membership Package Details {} is linked to this sales invoice").format(mmpd_name), raise_exception=True)
	else:			
		for item in doc.items:
			maintain_stock,quantity,validaity_in_days= frappe.db.get_value("Item",item.item_code,['is_stock_item','quantity','validaity_in_days']) or [0, 0,0]
			if cint(maintain_stock)==0 and cint(quantity)>0 and cint(validaity_in_days)>0:
				mpd_obj = frappe.new_doc("Membership Package Details")
				mpd_obj.member = doc.customer
				mpd_obj.sales_invoice = doc.name
				mpd_obj.package_name = item.item_code
				mpd_obj.start_date = today()
				mpd_obj.end_date = add_days(today(), cint(validaity_in_days))
				mpd_obj.quantity = quantity
				mpd_obj.flags.ignore_permissions = 1
				mpd_obj.insert()
	frappe.db.commit()

def cancel_si_membership_package_details(doc, method):
	for item in doc.items:
		mmpd_name= frappe.db.get_value("Membership Package Details",{"sales_invoice":doc.name,"package_name":item.item_code},"name")
		if mmpd_name:
			try:
				mpd_obj = frappe.get_doc("Membership Package Details",mmpd_name)
				mpd_obj.disabled=1
				mpd_obj.flags.ignore_permissions = 1
				mpd_obj.save()
			except Exception as e:
				msgprint(_("Membership Package Details {} is linked to this sales invoice").format(mmpd_name), raise_exception=True)
	frappe.db.commit()

def create_package_log():
	frappe.errprint("creating package logs")

	# for item in doc.items:
	# 	mmpd_name= frappe.db.get_value("Membership Package Details",{"sales_invoice":doc.name,"package_name":item.item_code},"name")
	# 	if mmpd_name:
	# 		try:
	# 			mpd_obj = frappe.get_doc("Membership Package Details",mmpd_name)
	# 			mpd_obj.disabled=1
	# 			mpd_obj.flags.ignore_permissions = 1
	# 			mpd_obj.save()
	# 		except Exception as e:
	# 			msgprint(_("Membership Package Details {} is linked to this sales invoice").format(mmpd_name), raise_exception=True)
	#frappe.db.commit()