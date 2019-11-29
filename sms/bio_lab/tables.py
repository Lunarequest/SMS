from django_tables2 import tables, TemplateColumn
from my_app.models import Training

class TrainingTable(tables.Table):
    class Meta:
         model = Training
         attrs = {'class': 'table table-sm'}
         fields = ['bio_eq_id', 'bio_eq_name', 'bio_eq_amount']

     edit = tables.LinkColumn('item_edit', args=[A('pk')], orderable=False)