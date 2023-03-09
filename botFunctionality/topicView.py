from .embeds import Embeds
from .pagination import PaginatedView
from .sheet import Sheet

class TopicView(PaginatedView):
    isActive: bool = False
    messageId: int = None

    def __init__(self, gSheet: Sheet, embedFactory: Embeds, data: list[dict], title:str, currentPage: int, currentIndex: int, itemsPerPage: int):
        super().__init__(gSheet, embedFactory, data, title, currentPage, currentIndex, itemsPerPage)

    def refreshData(self):
        try:
            self._data = self._gSheet.refetchTopicData(self.title)
        except:
            raise Exception('GSpread API Error: Could not refresh spreadsheet data. ❌')