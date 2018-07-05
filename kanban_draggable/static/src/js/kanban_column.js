odoo.define('kanban_draggable.kanban_column',function(require){
"use strict";

var config = require('web.config');
var KanbanColumn = require('web_kanban.Column');

KanbanColumn.include({
    start: function () {
        this._super.apply(this, arguments);

        if (this.record_options.sortable==false){
            this.$el.sortable("disable");
        }

        if (config.device.size_class > config.device.SIZES.XS && this.record_options.drag_drop==false && this.draggable==true){
            this.$el.sortable("option", "containment", "parent");
        }

    },

});
});