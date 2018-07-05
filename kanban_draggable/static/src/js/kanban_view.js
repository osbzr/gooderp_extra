odoo.define('kanban_draggable.kanban_view',function(require){
"use strict";


var KanbanRenderer = require('web_kanban.KanbanView');

KanbanRenderer.include({

    init: function () {
        this._super.apply(this, arguments);

        var arch = this.fields_view.arch;


        this.columns_sortable = true;
        if (arch.attrs.disable_sort_column) {
            if (arch.attrs.disable_sort_column=='true') {
                this.columns_sortable = false;
            }
        }
    },

    render_grouped: function (fragment) {
        var arch = this.fields_view.arch;

        this.record_options.drag_drop = true;
        if (arch.attrs.disable_drag_drop_record) {
            if (arch.attrs.disable_drag_drop_record=='true') {
                this.record_options.drag_drop = false;
            }
        }

        this.record_options.sortable = true;
        if (arch.attrs.disable_sort_record) {
            if (arch.attrs.disable_sort_record=='true') {
                this.record_options.sortable = false;
            }
        }

//        Call Super
        this._super.apply(this, arguments);
//        ........

        if (this.columns_sortable==false){
            this.$el.sortable("disable");
        }

    },

});

});