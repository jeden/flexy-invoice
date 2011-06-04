function addInvoiceItem() {
	var hInvoiceItems = $('#invoice-items') 
	var index = parseInt(hInvoiceItems.val()) + 1;
	$('#tbl-invoice-items tr:last').clone().find('input').each(function() {
		var newId = $(this).attr('id').replace(/^[\d]+/g, index);
		$(this).val('');
		$(this).attr('id', newId)
		$(this).attr('name', newId);
	}).end().appendTo('#tbl-invoice-items');
	hInvoiceItems.val(index)
}