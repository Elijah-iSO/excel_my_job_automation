from file_processing import (
    top_10, statements, receipts, receivable_overdue)

FILE_HANDLERS = {
    top_10: ('60', '62'),
    receivable_overdue: ('60', '62', '76'),
    receipts: ('50', '51', '52'),
    statements: ('pdf',)
}
