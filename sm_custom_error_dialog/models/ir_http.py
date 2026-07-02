# -*- coding: utf-8 -*-
from odoo import models

PARAM = "sm_custom_error_dialog.%s"


class IrHttp(models.AbstractModel):
    _inherit = "ir.http"

    def session_info(self):
        """Expose the error-dialog config so the frontend patch can read it
        synchronously at boot (no RPC, no race before the first error)."""
        result = super().session_info()
        icp = self.env["ir.config_parameter"].sudo()

        def get(key):
            return icp.get_param(PARAM % key) or ""

        result["sm_error_dialog"] = {
            "enabled": icp.get_param(PARAM % "enabled") in ("True", "true", "1"),
            "global_title": get("global_title"),
            "titles": {
                "odoo.exceptions.ValidationError": get("validation_title"),
                "odoo.exceptions.AccessError": get("access_title"),
                "odoo.exceptions.UserError": get("user_title"),
            },
        }
        return result
