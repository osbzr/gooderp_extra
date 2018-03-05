
var editor;


function createMySnippet() {
	return [

		{
			label: "oo_data",
			documentation: "Create the main tags",
			insertText: "<?xml version=\"1.0\" ?>\n<odoo>\n\t$1\n</odoo>"
		},
		{
			label: "oo_form",
			documentation: "Create form view",
			insertText: "<?xml version=\"1.0\" ?>\n<form string=\"$3\">\n\t<sheet>\n\t\t<group>\n\t\t\t<field name=\"$4\"/>\n\t\t</group>\n\t</sheet>\n</form>"
		},
		{
			label: "oo_tree",
			documentation: "Create tree view",
			insertText: "<?xml version=\"1.0\" ?>\n<tree string=\"$3\">\n\t<field name=\"$4\"/>\n</tree>"
		},
		{
			label: "oo_search",
			documentation: "Create search view",
			insertText: "<record id=\"$1_view_search\" model=\"ir.ui.view\">\n\t<field name=\"name\">$2.search</field>\n\t<field name=\"model\">$2</field>\n\t<field name=\"arch\" type=\"xml\">\n\t\t<tree string=\"$3\">\n\t\t\t<field name=\"$4\"/>\n\t\t\t<filter name=\"$5\" string=\"$6\" domain=\"[('$7', '=', $8), ]\"/>\n\t\t</tree>\n\t</field>\n</record>"
		},
		{
			label: "oo_form_inherit",
			documentation: "Inherit existing form view",
			insertText: "<!-- Inherit Form view -->\n<record id=\"$1\" model=\"ir.ui.view\">\n\t<field name=\"name\">$2.form</field>\n\t<field name=\"model\">$2</field>\n\t<field name=\"inherit_id\" ref=\"$3\"/>\n\t<field name=\"arch\" type=\"xml\">\n\t\t<field name=\"$4\" position=\"$5\">\n\t\t\t<!-- Add your fields or attributes here -->\n\t\t</field>\n\t</field>\n</record>"
		},
		{
			label: "oo_tree_inherit",
			documentation: "Inherit existing tree view",
			insertText: "<record id=\"$1\" model=\"ir.ui.view\">\n\t<field name=\"name\">$2.tree</field>\n\t<field name=\"model\">$2</field>\n\t<field name=\"inherit_id\" ref=\"$3\"/>\n\t<field name=\"arch\" type=\"xml\">\n\t\t<field name=\"$4\" position=\"$5\">\n\t\t\t<!-- Add new fields here -->\n\t\t</field>\n\t</field>\n</record>"
		},
		{
			label: "oo_search_inherit",
			documentation: "Inherit existing search view",
			insertText: "<record id=\"$1\" model=\"ir.ui.view\">\n\t<field name=\"name\">$2.search</field>\n\t<field name=\"model\">$2</field>\n\t<field name=\"inherit_id\" ref=\"$3\"/>\n\t<field name=\"arch\" type=\"xml\">\n\t\t<field name=\"$4\" position=\"$5\">\n\t\t\t<!-- Add new fields or filters here -->\n\t\t</field>\n\t</field>\n</record>"
		},
		{
			label: "oo_form_header",
			documentation: "Add Form's header with 'state' and buttons",
			insertText: "<header>\n\t<button name=\"$1\" string=\"$2\" class=\"oe_highlight\" states=\"$3\" type=\"$4\"/>\n\t<field name=\"state\" widget=\"statusbar\" statusbar_visible=\"$5\" statusbar_colors=\"{'KEY_IS_STATE':'VALUE_IS_COLOR'}\"/>\n</header>"
		},
		{
			label: "oo_action",
			documentation: "Create new action",
			insertText: "<record id=\"$1_action_form\" model=\"ir.actions.act_window\">\n\t<field name=\"name\">$2</field>\n\t<field name=\"res_model\">$3</field>\n\t<field name=\"view_mode\">tree,form</field>\n\t<field name=\"help\" type=\"html\">\n\t\t<p class=\"oe_view_nocontent_create\">\n\t\t\t<!-- Add Text Here -->\n\t\t</p>\n\t\t<p>\n\t\t\t<!-- More details about what a user can do -->\n\t\t</p>\n\t</field>\n</record>"
		},
		{
			label: "oo_menuitem_root",
			documentation: "Create menu item in the upper bar",
			insertText: "<menuitem id=\"menu_$1\" name=\"$2\" sequence=\"$3\"/>"
		},
		{
			label: "oo_menuitem_category",
			documentation: "Create menu item for category",
			insertText: "<menuitem id=\"menu_$1\" name=\"$2\" parent=\"$3\" sequence=\"$4\"/>"
		},
		{
			label: "oo_menuitem_action",
			documentation: "Create menu item for actions",
			insertText: "<menuitem id=\"menu_$1\" name=\"$2\" parent=\"$3\" action=\"$4\" sequence=\"$5\"/>"
		},
		{
			label: "oo_nested_group",
			documentation: "Add nested groups",
			insertText: "<group string=\"$1\">\n\t<group>\n\t\t<field name=\"$2\"/>\n\t</group>\n\t<group>\n\t\t<field name=\"$3\"/>\n\t</group>\n</group>"
		},
		{
			label: "oo_notebook",
			documentation: "Add notebook and a page",
			insertText: "<notebook>\n\t<page string=\"$1\">\n\t\t<group>\n\t\t\t<field name=\"$2\"/>\n\t\t</group>\n\t</page>\n</notebook>"
		},
		{
			label: "oo_page",
			documentation: "Add page",
			insertText: "<page string=\"$1\">\n\t<group>\n\t\t<field name=\"$2\"/>\n\t</group>\n</page>"
		},
		{
			label: "oo_domain",
			documentation: "Add domain to a field",
			insertText: "domain=\"[('$1', '=', $2), ]\""
		},
		{
			label: "oo_security_category",
			documentation: "Create security category",
			insertText: "\t\t    <record id=\"module_category_$1\" model=\"ir.module.category\">\n<field name=\"name\">$2</field>\n<field name=\"sequence\">$3</field>\n\t\t    </record>"
		},
		{
			label: "oo_security_group",
			documentation: "Create group, then assign new permissions",
			insertText: "<record id=\"group_$1\" model=\"res.groups\">\n\t<field name=\"name\">$2</field>\n\t<field name=\"category_id\" ref=\"$3\"/>\n\t<field name=\"implied_ids\" eval=\"[(4, ref('base.group_user'))]\"/>\n</record>"
		},
		{
			label: "oo_security_rule",
			documentation: "Create security rules",
			insertText: "<record id=\"rule_$1\" model=\"ir.rule\">\n\t<field name=\"name\">$2</field>\n\t<field name=\"model_id\" ref=\"model_$3\"/>\n\t<field name=\"domain_force\">[('$4', '=', $5), ]</field>\n\t<field name=\"perm_write\" eval=\"1\"/>\n\t<field name=\"perm_create\" eval=\"1\"/>\n\t<field name=\"perm_read\" eval=\"1\"/>\n\t<field name=\"perm_unlink\" eval=\"1\"/>\n\t<!-- You can attach this rule to a specific group, or make it global -->\n\t<field name=\"groups\" eval=\"[(4, ref('group_id'))]\"/>\n\t<!--<field name=\"global\" eval=\"1\"/> -->\n</record>"
		},
		{
			label: "oo_wkf",
			documentation: "Create workflow",
			insertText: "<record id=\"wkf_$1\" model=\"workflow\">\n\t<field name=\"name\">$2</field>\n\t<field name=\"osv\">$3</field>\n\t<field name=\"on_create\">True</field>\n</record>"
		},
		{
			label: "oo_wkf_transition",
			documentation: "Add transition to workflow",
			insertText: "<record id=\"trans_$1\" model=\"workflow.transition\">\n\t<field name=\"act_from\" ref=\"$2\"/>\n\t<field name=\"act_to\" ref=\"$3\"/>\n\t<field name=\"signal\">$4</field>\n</record>"
		},
		{
			label: "oo_wkf_activity",
			documentation: "Add activity to workflow",
			insertText: "<record id=\"act_$1\" model=\"workflow.activity\">\n\t<field name=\"wkf_id\" ref=\"$2\"/>\n\t<field name=\"name\">$3</field>\n\t<!--<field name=\"flow_start\">True</field>-->\n\t<!--<field name=\"flow_stop\">True</field>-->\n\t<field name=\"kind\">function</field>\n\t<field name=\"action\">$4</field>\n</record>"
		},
		{
			label: "oo_form_social",
			documentation: "Add Social Messaging and followers",
			insertText: "<div class=\"oe_chatter\">\n\t<field name=\"message_follower_ids\" widget=\"mail_followers\"/>\n\t<field name=\"message_ids\" widget=\"mail_thread\"/>\n</div>"
		},
		{
			label: "oo_smart_button_action",
			documentation: "Add Smart Button Type=Action",
			insertText: "                        <xpath expr=\"//div[@name='button_box']\" position=\"inside\">\n<!-->O posicionamento é na div sheet<-->\n                            <button type=\"action\" class=\"oe_stat_button\" icon=\"fa-money\"\n                                name=\"%(external name da action a ser chamada)d\"\n                                context=\"{'search_default_partner_id': active_id, 'default_partner_id': active_id}\">\n                                <field string=\"Bank account(s)\" name=\"bank_account_count\" widget=\"statinfo\"/>\n                            </button>\n                        </xpath>"
		}
	]
}

$(document).ready(function () {



	require.config({ paths: { 'vs': '/rozzi_monaco_editor/static/src/js/monaco/min/vs' } });
	require(['vs/editor/editor.main'], function () {

       /*  
		$.ajax({
			url: "/rozzi_monaco_editor/static/src/js/xml.json", success: function (result) {

				provideCompletionItems: () => {
					return result;

				}
					
				monaco.languages.registerCompletionItemProvider('xml',
					{
						provideCompletionItems: function (model, position) {
							// find out if we are completing a property in the 'dependencies' object.
							console.log($.parseJSON(result));
							return $.parseJSON(result);

						}
					}
				);
				
			}
		});

		$.ajax({
			url: "/rozzi_monaco_editor/static/src/js/python.json", success: function (result) {
				monaco.languages.registerCompletionItemProvider('python',
					{
						provideCompletionItems: function (model, position) {
							// find out if we are completing a property in the 'dependencies' object.
							console.log($.parseJSON(result));

							return $.parseJSON(result);

						}
					}
				);

			}
		});
		*/

		/*

		monaco.languages.registerCompletionItemProvider('xml', {
			provideCompletionItems: function(model, position) {
				// find out if we are completing a property in the 'dependencies' object.

				return createMySnippet();
				
			}
		});
		*/


		var txt;

		if ($('textarea[name="arch_base"]').length > 0) {
			txt = $('textarea[name="arch_base"]').val();

		}
		else {
			txt = $('.oe_form_text_content').text();
		}
		//alert(txt);



		editor = monaco.editor.create($('#container')[0], {
			value: [
				txt
			].join('\n'),
			language: 'xml'
		});
		$('.oe_form_field_text').css({ 'display': 'none' });

		$.ajax({
			url: "/rozzi_monaco_editor/static/src/js/xml.json", success: function (result) {

				monaco.languages.registerCompletionItemProvider('xml',
					{
						provideCompletionItems: () => {
							return $.parseJSON(result);

						}
					}
				);

			}
		});
		$.ajax({
			url: "/rozzi_monaco_editor/static/src/js/python.json", success: function (result) {

				monaco.languages.registerCompletionItemProvider('python',
					{
						provideCompletionItems: () => {
							return $.parseJSON(result);

						}
					}
				);

			}
		});


	});

	$('.oe_form_button_edit').bind("click", function () {
		//$('textarea[name="arch_base"]').css({'display':'none'});
		//editor.setValue($('textarea[name="arch_base"]').val()+'');
		$('.oe_form_field_text').css({ 'display': 'none' });

		$('#container').css({ 'display': '' });
		editor.setValue($('.oe_form_text_content').text());

		setTimeout(function () { $('.oe_form_field_text').css({ 'display': 'none' }); }, 2000)


	});


	$('.oe_form_button_save').bind("click", function () {
		$('textarea[name="arch_base"]').val(editor.getValue());
		$('textarea[name="arch_base"]').css({ 'display': '' });
		$('#container').css({ 'display': 'none' });


	});
});