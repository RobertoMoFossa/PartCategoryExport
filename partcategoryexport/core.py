from plugin import InvenTreePlugin
from plugin.mixins import DataExportMixin
from part.models import PartCategory


class PartCategoryPassThrough(DataExportMixin, InvenTreePlugin):
    """
    Pass-through exporter for Part Categories.

    IMPORTANT:
    - Does NOT override update_headers
    - Does NOT override export_data
    - Uses the EXACT same export pipeline as the official InvenTree Exporter
    """

    TITLE = "PartCategory Pass-Through (Test)"
    NAME = "PartCategoryPassThrough"
    SLUG = "partcategory-passthrough"
    DESCRIPTION = (
        "Test exporter that returns exactly the same data as the official exporter"
    )
    VERSION = "0.1.1"

    def supports_export(self, model_class, user, *args, **kwargs):
        return issubclass(model_class, PartCategory)
