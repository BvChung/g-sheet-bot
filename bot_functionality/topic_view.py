from .embeds import Embeds
from .pagination import PaginatedView
from .sheet import Sheet

class TopicView(PaginatedView):
    is_active: bool = False
    message_id: int = None

    def __init__(self, google_sheets: Sheet, embed_factory: Embeds, data: list[dict], title:str, current_page: int, current_index: int, items_per_page: int):
        super().__init__(google_sheets, embed_factory, data, title, current_page, current_index, items_per_page)

    def refresh_data(self):
        try:
            self._data = self._google_sheets.refetch_topic_data(self.title)
        except Exception as error:
            raise Exception(f'GSpread API Error: Could not refresh spreadsheet data. ❌\n{error}')