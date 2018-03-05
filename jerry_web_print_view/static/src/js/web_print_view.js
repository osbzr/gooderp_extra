odoo.define('web_print_view.web_print_view', function(require) {
    "use strict";
    var core = require('web.core');
    var QWeb = core.qweb;
    var _t = core._t;
    var Sidebar = require('web.Sidebar');
    var formats = require('web.formats');
    var ListView = require('web.ListView');






    ListView.include({

        load_list: function() {

            var rst=this._super();
            $($(this.$el.find('.o_list_view')).find('th')[0]).prepend(QWeb.render('AddExport', {widget: self}));
            $($(this.$el.find('.o_list_view')).find('th')[0]).css({"min-width":"100px"});
            this.$el.find('.oe_export_table').on('click', this.on_export_table);

            //alert('load_list');

            return rst;

        },




        on_export_table: function () {
            // Select the first list of the current (form) view
            // or assume the main view is a list view and use that
            //alert('on_sidebar_export_view_xls');


            var self = this,
                view = this,

                children = view.getChildren();


            if (children) {
                children.every(function (child) {
                    if (child.field && child.field.type == 'one2many') {
                        view = child.viewmanager.views.list.controller;
                        return false; // break out of the loop
                    }
                    if (child.field && child.field.type == 'many2many') {
                        view = child.list_view;
                        return false; // break out of the loop
                    }
                    return true;
                });
            }
            var export_columns_keys = [];
            var export_columns_names = [];



            var head=$(view.$el.find('tr')[0]);

            //解决web_list_view_sticky模块可能引起的多header问题

            var ths=$(head[0]).find('th');
            var skipid=-1;
            var isgroup=view.$el.find('.o_list_view_grouped').length;

            for(var i=0;i<ths.length;i++)
            {
                console.log($(ths[i]));
                if($(ths[i]).find('.o_checkbox').length>0)
                {
                    skipid=i;

                }
                else
                {
                    export_columns_keys.push(i);
                    export_columns_names.push($(ths[i]).text().trim());
                }
            }

            //export_columns_names[0]=export_columns_names[0].replace('导出','').trim();



            var rows = view.$el.find(' tbody > tr');
            var export_rows = [];
            $.each(rows, function () {
                var $row = $(this);
                // find only rows with data
                //if ($row.attr('data-id')) {
                if (1) {

                    var export_row = [];

                    //cell = $row.find('th').get(0);
                    //text = cell.text || cell.textContent || cell.innerHTML || "";
                    //export_row.push(text);

                    var cells=$row.find('td,th');
                    for(var i=0;i<cells.length;i++)
                    {
                        if(i==skipid) continue;
                        var cell = cells.get(i);
                        var text =  cell.text || cell.textContent || cell.innerHTML ||  "";

                        if(cell.classList.contains("oe_list_group_pagination"))
                        {
                            export_row.push(text.trim());
                        }
                        else if (cell.classList.contains("oe_list_field_float")||cell.classList.contains("o_list_number")||cell.classList.contains("oe_number")) {
                            export_row.push(formats.parse_value(text, {'type': "float"}, 0));
                        }
                        else if (cell.classList.contains("oe_list_field_boolean")) {
                            var data_id = $('<div>' + cell.innerHTML + '</div>');
                            if (data_id.find('input').get(0).checked) {
                                export_row.push('是');
                            }
                            else {
                                export_row.push('否');
                            }
                        }
                        else if (cell.classList.contains("oe_list_field_integer")) {
                            var tmp2 = text;
                            export_row.push(parseInt(tmp2));
                        }
                        else {
                            if(i>0)
                            {
                                export_row.push(text.trim());
                            }
                            else
                            {
                                if(isgroup){
                                    text=text.replace(/(\s*$)/g, "");
                                    export_row.push(text);

                                }
                                else
                                {
                                    export_row.push(text.trim());
                                }



                            }
                        }

                    }
                    export_rows.push(export_row);
                }
            });
            $.blockUI();
            view.session.get_file({
                url: '/web/export/xls_view',
                data: {data: JSON.stringify({
                    model: view.model,
                    headers: export_columns_names,
                    rows: export_rows
                })},
                complete: $.unblockUI
            });
        },

        /*

        pad_columns: function (count, options) {

            //alert('pad_columns');
            this._super(count, options);
            $($('.o_list_view').find('th')[0]).prepend(QWeb.render('AddExport', {widget: self}));
            $($('.o_list_view').find('th')[0]).css({"width":"100px"});
            this.$el.find('.oe_export_table').on('click', this.on_export_table);
        },
        */





        render_sidebar: function() {
            //alert('render_sidebar');
            /*
            function mytimer () {
                    if($('.oe-cp-sidebar > div').length==0)
                    {
                        setTimeout(mytimer,10000);
                    }else
                    {
                        $('.oe-cp-sidebar > div').removeClass("o_hidden");
                        $('.oe-cp-sidebar > div').css({"display": "block !important;"});
                    }
            };
            */

            this._super.apply(this, arguments);
            if(this.sidebar) this.sidebar.do_show();

            /*

            console.log($('.o_list_view'));

            //console.log($($(this.$el('.o_list_view')).find('.o_list_view >th')[0]));
            $($(this.$el.find('.o_list_view')).find('th')[0]).prepend(QWeb.render('AddExport', {widget: self}));
            $($(this.$el.find('.o_list_view')).find('th')[0]).css({"width":"100px"});
            console.log($(this.$el.find('.o_list_view >th')[0]));
            this.$el.find('.oe_export_table').on('click', this.on_export_table);
            */

        }
    });

    Sidebar.include({

        do_hide: function() {


        },
        redraw: function () {
            $($(this.$el.find('.o_list_view')).find('th')[0]).prepend(QWeb.render('AddExport', {widget: self}));
            $($(this.$el.find('.o_list_view')).find('th')[0]).css({"width":"100px"});
            //alert('redraw');
            //console.log($.find('.o_list_view'));

            var self = this;
            this._super.apply(this, arguments);
            if (self.getParent().ViewManager.active_view.type == 'list') {

                self.$el.find('.o_cp_sidebar').append(QWeb.render('AddPrintViewMain', {widget: self}));
                self.$el.find('.o_dropdown').last().append(QWeb.render('AddPrintViewMain', {widget: self}));
                self.$el.find('.oe_sidebar_print_view').on('click', self.on_sidebar_print_view);
                self.$el.find('.oe_sidebar_expand_group').on('click', self.on_sidebar_expand_group);
                self.$el.find('.oe_sidebar_collapse_group').on('click', self.on_sidebar_collapse_group);


            }
            else
            {
                self.$el.find('.o_cp_sidebar').append('111111111111');
                self.$el.find('.o_cp_sidebar').append(QWeb.render('AddPrintViewMain', {widget: self}));
                self.$el.find('.o_dropdown').last().append(QWeb.render('AddPrintViewMain', {widget: self}));
                self.$el.find('.oe_sidebar_print_view').on('click', self.on_sidebar_print_view);

                //查找 .nav-tabs
                //  <input class="oe_print_selector" title="print?" type="checkbox">

                /*

                console.log(self.$el.find('.nav-tabs'));
                console.log($('.nav-tabs'));
                console.log($('ul .nav-tabs'));


                console.log($('.nav-tabs > li'));
                console.log($('.o_list_view'));
                */




                $.each($('.nav-tabs > li a'),function(el) {

                    if($(this).find('input').length==0)
                        $(this).html('<input class="oe_print_selector" title="print?" type="checkbox" checked>'+$(this).html());

                });



                $('.oe_print_selector').on('click',function (e) {
                    e.stopPropagation();
                    var checked = $(e.currentTarget).find('input').prop('checked');
                    $(e.currentTarget).attr('checked',! checked);
                });








            }
        },

        on_sidebar_expand_group:function(){

            $.each($('.o_group_header'),function(el) {

                if($(this).find('.fa-caret-right').length>0)
                {
                    this.click();
                }
            });
        },

        on_sidebar_collapse_group:function(){

            $.each($('.o_group_header'),function(el) {
                    this.click();

            });
        },

        on_sidebar_print_view: function () {
            // Select the first list of the current (form) view
            // or assume the main view is a list view and use that


            var self = this,
                view = this.getParent(),
                children = view.getChildren();


            $('.oe-button-column').css({"display":"none"});
            $('.oe-right-toolbar').css({"display":"none"});
            $('.tab-pane').css({"display":"block"});
            $('.o_chatter').css({"display":"none"});
            $('.oe_list_sidebar').css({"display":"none"});

            $('.o_web_client > .o_main .o_main_content .o_content').css({"overflow":"visible"});
            $('.o_form_view .o_form_sheet_bg .o_form_sheet').css({"border":"0"});



            if (self.getParent().ViewManager.active_view.type == 'list') {
                $('.oe-search-options').css({"display":"none"});

            }


            //找到 nav-tabs 并取出它的html


            for(var j=0;j<$('.nav-tabs li').length;j++) {
                    $($('.nav-tabs li')[j]).removeClass('active');
            }
            $($('.nav-tabs li')[0]).addClass('active');

            $('.nav-tabs >li').css({"display":"none"});
            $('header').css({"display":"none"});
            $('header').css({"display":"none"});




            for(var i=0;i<$('.tab-pane').length;i++)
            {

                var toprint=$($('.oe_print_selector')[i]).prop('checked');
                if(!toprint)
                {
                    $($('.tab-pane')[i]).css({"display":"none"});
                    continue;
                }


                var tabshtml=$('.nav-tabs').html();
                var tabsobj=$(tabshtml);
                for(var j=0;j<tabsobj.length;j++) {
                    $(tabsobj[j]).removeClass('active');

                    $(tabsobj[j]).css({"display":"block"});

                    if(!$($('.oe_print_selector')[j]).prop('checked'))
                    {
                        ($(tabsobj[j]).find('input')).attr('checked',false);
                    }
                }


                $(tabsobj[i]).addClass('active');
                var ulobj=$('<ul role="tablist" class="nav nav-tabs myaddul" style="padding-top: 20px;"></ul>');

                var temp=ulobj.append(tabsobj);

                $($('.tab-pane')[i]).prepend(temp);

            }





            window.print();

            //恢复现场

            $('.oe-button-column').css({"display":""});
            $('.oe-right-toolbar').css({"display":""});
            $('.tab-pane').css({"display":""});

            $('.o_chatter').css({"display":""});

            if (self.getParent().ViewManager.active_view.type == 'list') {
                $('.oe-search-options').css({"display":""});
            }

            $('.oe_list_sidebar').css({"display":""});
            $('.nav-tabs >li').css({"display":""});
            $('header').css({"display":""});

            for(var i=$('.myaddul').length-1;i>=0;i--)
            {
                $('.myaddul')[i].remove();
            }










        }
    })

});
