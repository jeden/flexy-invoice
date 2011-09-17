function setGridParams(caption, pagerId) {
	return {
		datatype: 'json',
		rowNum: 25,
		rowList: [25, 50, 100],
		pager: pagerId,
		viewrecords: true,
		caption: caption,
		autowidth: true,
		height: '500px',
		jsonReader: {
			repeatitems: false
		},
		toolbar: [true, 'top'],
//		onSelectRow: function(rowid, status) { viewRequest('#dialog', rowid); },
	};
}