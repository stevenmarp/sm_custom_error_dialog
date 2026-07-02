# -*- coding: utf-8 -*-
from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    sm_ed_enabled = fields.Boolean(
        string="Customize error dialog titles",
        config_parameter="sm_custom_error_dialog.enabled",
    )
    sm_ed_global_title = fields.Char(
        string="Global title",
        config_parameter="sm_custom_error_dialog.global_title",
        help="Applied to every error dialog. Per-type titles below override it.",
    )
    sm_ed_validation_title = fields.Char(
        string="Validation Error title",
        config_parameter="sm_custom_error_dialog.validation_title",
    )
    sm_ed_access_title = fields.Char(
        string="Access Error title",
        config_parameter="sm_custom_error_dialog.access_title",
    )
    sm_ed_user_title = fields.Char(
        string="User Error title",
        config_parameter="sm_custom_error_dialog.user_title",
    )
