from waitress import serve
from euf.wsgi import application
import warnings

warnings.filterwarnings("ignore")

serve(application, host="0.0.0.0", port=8001)
