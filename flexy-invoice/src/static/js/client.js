function loadClientsGrid(caption, tableId, pagerId) {
	var table = $(tableId);
	table.jqGrid({
		url: '/p/async/client/list',
		datatype: 'json',
		colModel: [
		           {name: 'name'},
		           {name: 'address'},
		           {name: 'email'},
		           {name: 'default_currency'},
		           {name: 'default_language'}
		],
		colNames: ['Name', 'Address', 'Email', 'Default Currency', 'Default Language'],
		rowNum: 25,
		rowList: [25, 50, 100],
		pager: pagerId,
		sortName: 'name',
		viewrecords: true,
		caption: caption,
		autowidth: true,
		height: '500px',
		jsonReader: {
			repeatitems: false
		},
		toolbar: [true, 'top'],
//		onSelectRow: function(rowid, status) { viewRequest('#dialog', rowid); },
	});
}