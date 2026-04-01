"""A short description of the project"""

from plugin import InvenTreePlugin
from collections import OrderedDict
from typing import Any

from django.db.models import QuerySet
from plugin.mixins import DataExportMixin

from part.models import PartCategory

from . import PLUGIN_VERSION


class PartCategoryExport(DataExportMixin, InvenTreePlugin):
    """PartCategoryExport - custom InvenTree plugin."""

    # Plugin metadata
    TITLE = "PartCategoryExport"
    NAME = "PartCategoryExport"
    SLUG = "partcategoryexport"
    DESCRIPTION = "A short description of the project"
    VERSION = PLUGIN_VERSION

    # Additional project information
    AUTHOR = "Roberto"
    WEBSITE = "https://my-project-url.com"
    LICENSE = "MIT"

    def supports_export(self, model_class, user, *args, **kwargs) -> bool:
        return issubclass(model_class, PartCategory)

    def update_headers(
        self, headers: OrderedDict, context: dict, **kwargs
    ) -> OrderedDict:
        # Solo asegurar que existen (sin romper nada)
        headers.setdefault("name", "Name")
        headers.setdefault("description", "Description")
        headers.setdefault("pathstring", "Path")
        headers.setdefault("partcount", "Parts")
        return headers

    def export_data(
        self,
        queryset: QuerySet,
        serializer_class,
        headers: OrderedDict,
        context: dict,
        output: Any,
        **kwargs,
    ) -> list[dict]:
        data = []

        for cat in queryset:
            data.append({
                "name": cat.name,
                "description": cat.description or "",
                "pathstring": cat.pathstring,
                "partcount": getattr(cat, "partcount", 0),
            })

        return data
