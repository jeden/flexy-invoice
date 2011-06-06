var invoiceItemTemplate;

function addInvoiceItem() {
	var hInvoiceItems = $('#invoice-items') 
	var index = parseInt(hInvoiceItems.val()) + 1;
	var newRowId = 'invoice-items-row' + index;

	var table = $('#tbl-invoice-items');
	var newRow = invoiceItemTemplate.clone().attr('id', newRowId);

	newRow.find('input').each(function() {
		var newId = $(this).attr('id').replace(/^[\d]+/g, index);
		$(this).val('');
		$(this).attr('id', newId)
		$(this).attr('name', newId);
	}).end().appendTo('#tbl-invoice-items');

	hInvoiceItems.val(index);
	dojo.parser.parse(dojo.byId(newRowId));
}

function loadInvoiceItemTemplate()
{
	invoiceItemTemplate = $('#tbl-invoice-items tr:last').clone();
}