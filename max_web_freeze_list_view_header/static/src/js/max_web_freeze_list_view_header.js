odoo.define('max_web_freeze_list_View_header', function (require) {
'use strict';

    var ListView = require('web.ListView');

    ListView.include({
        load_list: function () {
            var self = this;
            return this._super.apply(this, arguments).done(function () {
                var form_field_length = self.$el.parents('.o_form_field').length;
                var scrollArea = $(".o_content")[0];
                function do_freeze () {
                    self.$el.find('table.o_list_view').each(function () {
                        $(this).stickyTableHeaders({scrollableArea: scrollArea, fixedOffset: 0.1});
                    });
                }

                if (form_field_length == 0) {
                    do_freeze();
                    $(window).unbind('resize', do_freeze).bind('resize', do_freeze);
                }
            });
        },
    })

    ListView.Groups.include({
        render_groups: function () {
            var self = this;
            var placeholder = this._super.apply(this, arguments);
            var grouping_freezer = document.createElement("script");

            grouping_freezer.innerText = "$('.o_group_header').click(function () {"
                + " setTimeout(function () { $(window).resize(); }, 200); })";

            placeholder.appendChild(grouping_freezer);
            return placeholder;
        },
    });
});
