odoo.define('web_menu_hide', function (require) {

    var core = require('web.core'),
        QWeb = core.qweb,
        _t = core._t,
        client = require('web.WebClient');

    client.include({

        bind_events: function () {
            var self = this;
            this._super();
            elem=$("<ul class='nav navbar-nav navbar-left'><li style='display: block;' ><a id='web_menu_hideshow' href='#' title='Show/Hide left menu' class='web_hide_show'/></li></ul>");
            root=self.$el.parents();
            elem.prependTo(root.find('.oe_application_menu_placeholder'));
            self.$el.on('click', '#web_menu_hideshow', function () {
                // Check if left menu visible
                root=self.$el.parents();
                var visible=(root.find('.o_sub_menu').css('display') != 'none');
                if (!visible) {
                    // Show menu and resize form components to original values
                    root.find('.o_sub_menu').css('display', 'flex');
                    root.find('.o_form_sheet_bg').css('padding', self.sheetbg_padding);
                    root.find('.o_form_sheet').css('max-width', self.sheetbg_maxwidth);
                    root.find('.o_form_view div.o_chatter').css('max-width', self.chatter_maxwidth);
                    root.find('.o_followers').css('width', self.followers_width);
                    root.find('.o_mail_thread').css('margin-right', self.record_thread_margin);
                } else {
                    // Hide menu and save original values
                    root.find('.o_sub_menu').css('display', 'none');
                    self.sheetbg_padding=root.find('.oe_form_sheetbg').css('padding');
                    root.find('.o_form_sheet_bg').css('padding', '16px');
                    self.sheetbg_maxwidth=root.find('.oe_form_sheet_width').css('max-width');
                    root.find('.o_form_sheet').css('max-width', '100%');
                    self.chatter_maxwidth=root.find('.oe_form div.oe_chatter').css('max-width');
                    root.find('.o_form_view div.o_chatter').css('max-width','100%');
                    self.followers_width=root.find('.oe_followers').css('width');
                    root.find('.o_followers').css('width', '250px');
                    self.record_thread_margin=root.find('.oe_record_thread').css('margin-right');
                    root.find('.o_mail_thread').css('margin-right', '293px');
                }

            });
        }

    });

});