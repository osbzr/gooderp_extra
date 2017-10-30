odoo.define('max_web_select_list_view_column', function (require) {
'use strict';

var core = require('web.core');
var ListView = require('web.ListView');
var Model = require('web.DataModel');
var QWeb = core.qweb;

ListView.include({
    init: function () {
        this._super.apply(this, arguments);
        var self = this;
        self.column_settings = new Model('max.web.select.list.view.column.setting');
    },

    reload: function () {
        this.setup_columns(this.fields_view.fields, this.grouped);
        this.$el.html(QWeb.render(this._template, this));
        return this.reload_content();
    },

    render_buttons: function ($node) {
        var self = this;
        this._super($node);
        this.$buttons.find('.oe_select_columns').click(this.proxy('render_column_list'));
        this.$buttons.find('.oe_apply_btn').click(this.proxy('apply_columns'));
        this.$buttons.find('.oe_reset_btn').click(this.proxy('reset_columns'));
        this.$buttons.find('.oe_dropdown_menu').click(this.proxy('stop_event'));
    },

    render_column_list: function (fields, grouped) {
        $("#showcb").show();
        var getcb = document.getElementById('showcb');
        this.visible_columns = _.filter(this.columns, function (column) {
            var firstcheck = document.getElementById(column.id);
            if (firstcheck == null) {
                var li = document.createElement("li");
                var description = document.createTextNode(column.string);
                var checkbox = document.createElement("input");
                checkbox.id = column.id;
                checkbox.type = "checkbox";
                checkbox.name = "cb";

                if (column.invisible !== '1') {
                    checkbox.checked = true;
                }
                li.appendChild(checkbox);
                li.appendChild(description);
                getcb.appendChild(li);
            }
            else {
                if (column.invisible !== '1') {
                    firstcheck.checked = true;
                }
                else {
                    firstcheck.checked = false;
                }
            }
        });
    },

    stop_event: function (e) {
        e.stopPropagation();
    },

    apply_columns: function () {
        var self = this;
        $("#showcb").hide();
        var column_ids = [];
        _.each($('.oe_dropdown_menu li input'), function (c) {
            var ch = $(c);
            if (typeof ch != 'undefined') {
                if ($(ch)[0].checked) {
                    column_ids.push($(ch)[0].id)
                }
            }
        });
        function check_columns() {
            if (column_ids.length < 1) {
                setTimeout(check_columns, 100);
            }
            else {
                var action_context = self.ViewManager.action;
                self.column_settings.call('save_columns', [[], {
                    'name': action_context.display_name,
                    'xml_id': action_context.xml_id,
                    'res_model': action_context.res_model,
                    'user_id': self.dataset.context.uid
                }, column_ids, self.dataset.context]).then(function () {
                    return self.reload();
                });
            }
        }

        check_columns();
    },

    reset_columns: function () {
        var self = this;
        $("#showcb").hide();

        var action_context = self.ViewManager.action;
        self.column_settings.call('reset_columns', [[], {
            'name': action_context.display_name,
            'xml_id': action_context.xml_id,
            'res_model': action_context.res_model,
            'user_id': self.dataset.context.uid
        },
            self.dataset.context]).then(function () {
            return self.reload();
        });
    },

    setup_columns: function (fields, grouped) {
        this._super(fields, grouped);
        var self = this;
        var action_context = self.ViewManager.action;
        if (action_context === undefined)
            return;
        self.column_settings.call('get_columns', [[], {
            'name': action_context.display_name,
            'xml_id': action_context.xml_id,
            'res_model': action_context.res_model,
            'user_id': this.dataset.context.uid
        }]).then(function (stored_cols) {
            if (stored_cols.length > 0) {
                self.visible_columns = _.filter(self.columns, function (column) {
                    var column_checkbox_id = document.getElementById(column.id);
                    if (column_checkbox_id !== null) {
                        var column_visible = column_checkbox_id.checked;
                        if (column_visible !== false) {
                            column.invisible = '2';
                        }
                        else {
                            column.invisible = '1';
                        }
                    }
                    if ($.inArray(column.name, stored_cols) > -1) {
                        column.invisible = '2';
                    }
                    else {
                        column.invisible = '1';
                    }
                    return column.invisible !== '1';
                });
                self.aggregate_columns = _(self.visible_columns).invoke('to_aggregate');
            }
        });
    },
});

$(document).click(function() {
    $("#showcb").hide();
});

});
