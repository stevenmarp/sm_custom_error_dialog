# -*- coding: utf-8 -*-
{
    "name": "Custom Error Dialog",
    "version": "19.0.1.0.0",
    "category": "Productivity",
    "summary": "Rename Odoo error dialog titles (Validation, Access, User, and all errors) from Settings",
    "description": """
Custom Error Dialog
===================

Replace the default Odoo error popup titles with your own wording, configured
from Settings — no code, no per-model patching.

Features
--------
* Enable/disable from Settings, live via session (no server restart)
* One global title applied to every error dialog
* Per-type overrides for Validation, Access, and User errors
* Matches errors by exception type, not by translated string
* Zero overhead when disabled (no patch applied)
    """,
    "author": "Steven Marp",
    "website": "https://apps.odoo.com/apps/modules/browse?author=Steven Marp",
    "license": "OPL-1",
    "depends": ["web", "base_setup"],
    "data": [
        "views/res_config_settings_views.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "sm_custom_error_dialog/static/src/js/error_dialog_patch.js",
        ],
    },
    "images": [
        "static/description/banner.gif",
        "static/description/icon.png",
    ],
    "installable": True,
    "application": False,
    "auto_install": False,
    "price": 39.73,
    "currency": "USD",
}
