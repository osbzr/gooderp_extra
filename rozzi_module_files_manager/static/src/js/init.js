//"use strict";

var editor = null, diffEditor = null;

function get_file_list() {
	$.ajax({
		url: "/rozzi_module_files_manager/get_file_list?m=" + $('#div_m').text().trim(),
		success: function (result) {

			result = $.parseJSON(result);
			var html = '';

			for (var i = 0; i < result.files.length; i++) {
				html += '<option value="' + result.files[i] + '">' + result.files[i] + '</option>';

			}
			$('#file_name').html(html);

		}
	});
}

function read_file() {
	
	var canreadArr=['py','xml','js','html','htm','md','rst','md','po','txt','csv','yml','css'];
	var filename=$('#file_name').val();

	var ext=filename.split('.')[1]

	if(canreadArr.indexOf(ext)<0)
	{
		alert('Can not read file of this type !');
		return;
	}
	

	$.ajax({
		url: "/rozzi_module_files_manager/read_file?m=" + $('#div_m').text().trim() + '&f=' + filename,
		success: function (result) {

			result = $.parseJSON(result);

			//editor.setValue(result.data);


			if (!editor) {
				$('#container').empty();
				editor = monaco.editor.create(document.getElementById('container'), {
					model: null,
				});
			}


			var lang='python';
			

			if(filename.indexOf('.py')>0)
			{
				lang='python';
			}
			else if(filename.indexOf('.xml')>0)
			{
				lang='xml';
			}
			else if(filename.indexOf('.js')>0)
			{
				lang='javascript';
			}

			var oldModel = editor.getModel();
			var newModel = monaco.editor.createModel(result.data, lang);
			editor.setModel(newModel);
			if (oldModel) {
				oldModel.dispose();
			}
			$('.loading.editor').fadeOut({ duration: 300 });
			editor.layout();
			
			$('#file_type').val(lang);
			


		}
	});
}
function save_file() {
	var filename=$('#file_name').val();
	

	$.ajax({
		url: "/rozzi_module_files_manager/save_file",
		type: 'POST',
		data:{
			m:$('#div_m').text().trim() ,
			f:filename,
			data:editor.getValue()
		},

		success: function (result) {

			alert(result);

		},
		error:function(error) { 
			alert('发生错误\n\r'+$.strinify()); 
		}
	});
}



function loadSample(mode) {
	//$('.loading.editor').show();

	if (!editor) {
		$('#container').empty();
		editor = monaco.editor.create(document.getElementById('container'), {
			model: null,
		});
	}

	var oldModel = editor.getModel();
	var newModel = monaco.editor.createModel(editor.getValue(), mode.modeId);
	editor.setModel(newModel);
	if (oldModel) {
		oldModel.dispose();
	}
	//$('.loading.editor').fadeOut({ duration: 300 });

}


$(document).ready(function () {
	$('#module_name').val($('.oe_form_char_content').eq(3).html());
	get_file_list();

	require.config({ paths: { 'vs': '/rozzi_monaco_editor/static/src/js/monaco/min/vs' } });
	require(['vs/editor/editor.main'], function () {

		var MODES = (function () {
			var modesIds = monaco.languages.getLanguages().map(function (lang) { return lang.id; });
			modesIds.sort();

			return modesIds.map(function (modeId) {
				return {
					modeId: modeId,
					sampleURL: 'index/samples/sample.' + modeId + '.txt'
				};
			});
		})();

		var startModeIndex = 0;
		for (var i = 0; i < MODES.length; i++) {
			var o = document.createElement('option');
			o.textContent = MODES[i].modeId;
			if (MODES[i].modeId === 'typescript') {
				startModeIndex = i;
			}
			$(".language-picker").append(o);
		}
		$(".language-picker")[0].selectedIndex = startModeIndex;
		loadSample(MODES[startModeIndex]);



		$(".language-picker").change(function () {
			loadSample(MODES[this.selectedIndex]);
		});


		$(".file_name").change(function () {
			read_file();
		});
		

		/*

        $('#container').empty();
			editor = monaco.editor.create(document.getElementById('container'), {
				model: null,
			});
		*/

		/*
		editor = monaco.editor.create(document.getElementById('container'), {
			value: [
				"loading......"
			].join('\n'),
			language: 'xml'
		});
		*/
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

		$(".language-picker").change(function () {
			loadSample(MODES[this.selectedIndex]);
		});

		$(".div_m").change(function () {
			//loadSample(MODES[this.selectedIndex]);
			get_file_list() ;
		});

		



	});




});