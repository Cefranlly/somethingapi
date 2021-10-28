import os
from alembic import op

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'files/interview_data.csv')
# TODO: Improve method to include csv separator and other things
op.execute(f"copy interview_data FROM '{file_name}' WITH CSV;", execution_options=None)
