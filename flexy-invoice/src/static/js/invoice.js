var invoiceItemTemplate;

function addInvoiceItem() {
	var hInvoiceItems = $('#invoice-items');
	var index = parseInt(hInvoiceItems.val()) + 1;

	var hLastInvoiceItemIndex = $('#h-last-invoice-item-index');
	var lastInvoiceItemIndex = parseInt(hLastInvoiceItemIndex.val()) + 1;
	
	var newRowId = 'invoice-items-row' + lastInvoiceItemIndex;

	var table = $('#tbl-invoice-items');
	var newRow = invoiceItemTemplate.clone().attr('id', newRowId);

	newRow.find('input').each(function() {
		var newId = $(this).attr('id').replace(/^[\d]+/g, lastInvoiceItemIndex);
		$(this).val('');
		$(this).attr('id', newId);
		$(this).attr('name', newId);
	}).end().appendTo('#tbl-invoice-items');

	$('#' + lastInvoiceItemIndex + '_btn-remove-invoice-item').attr('onClick', 'deleteInvoiceItem(' + lastInvoiceItemIndex + ')');
	
	hInvoiceItems.val(index);
	hLastInvoiceItemIndex.val(lastInvoiceItemIndex);
	dojo.parser.parse(dojo.byId(newRowId));
}

function deleteInvoiceItem(row_number)
{
	var hInvoiceItems = $('#invoice-items'); 
	var currentInvoiceItems = parseInt(hInvoiceItems.val());
	
	$('#invoice-items-row' + row_number).remove();

	hInvoiceItems.val(currentInvoiceItems - 1);
}

function loadInvoiceItemTemplate()
{
	invoiceItemTemplate = $('#tbl-invoice-items tr:last').clone();
}