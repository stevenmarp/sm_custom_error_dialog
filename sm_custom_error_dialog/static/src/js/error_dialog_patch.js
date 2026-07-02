/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { session } from "@web/session";
import {
    ClientErrorDialog,
    ErrorDialog,
    NetworkErrorDialog,
    RPCErrorDialog,
    WarningDialog,
} from "@web/core/errors/error_dialogs";

const cfg = session.sm_error_dialog || {};

// Only patch when enabled — disabled = original Odoo behavior, zero overhead.
if (cfg.enabled) {
    const titles = cfg.titles || {};
    const globalTitle = cfg.global_title || "";

    // Per-type override wins, then the global title, then Odoo's own title.
    const resolve = (exceptionName, fallback) =>
        (exceptionName && titles[exceptionName]) || globalTitle || fallback;

    // ValidationError / AccessError / UserError render through WarningDialog;
    // its header title is `this.title`.
    patch(WarningDialog.prototype, {
        setup() {
            super.setup(...arguments);
            this.title = resolve(this.props.exceptionName, this.title);
        },
    });

    // Server tracebacks render through RPCErrorDialog; the body title is `this.title`.
    patch(RPCErrorDialog.prototype, {
        setup() {
            super.setup(...arguments);
            this.title = resolve(this.props.exceptionName, this.title);
        },
    });

    // Generic client/network/script dialogs carry no exception name and read
    // their static class title — override it so the global title reaches them too.
    if (globalTitle) {
        ErrorDialog.title = globalTitle;
        ClientErrorDialog.title = globalTitle;
        NetworkErrorDialog.title = globalTitle;
    }
}
