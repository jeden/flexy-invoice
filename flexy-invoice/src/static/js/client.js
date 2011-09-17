function loadClientsGrid(caption, tableId, pagerId) {
	var params_base = setGridParams(caption, pagerId);
	var params_spec = {
		url: '/p/async/client/list',
		colModel: [
		           {name: 'name'},
		           {name: 'address'},
		           {name: 'email'},
		           {name: 'default_currency'},
		           {name: 'default_language'}
		],
		colNames: ['Name', 'Address', 'Email', 'Default Currency', 'Default Language'],
		sortName: 'name',
	};
	
	$(tableId).jqGrid($.extend(params_base, params_spec));
}