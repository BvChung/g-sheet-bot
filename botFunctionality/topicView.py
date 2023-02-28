import sys
from .embeds import Embeds
from .pagination import PaginatedView
from .sheet import Sheet

class TopicView(PaginatedView):
    instance = None
    messageId: int = sys.maxsize

    def __init__(self, gSheet: Sheet, embedFactory: Embeds, data: list[dict], title:str, currentPage: int, currentIndex: int, itemsPerPage: int):
        super().__init__(gSheet, embedFactory, data, title, currentPage, currentIndex, itemsPerPage)

    @staticmethod
    def getState(gSheet: Sheet, embedFactory: Embeds, data: list[dict], title:str, currentPage: int, currentIndex: int, itemsPerPage: int):
        if not TopicView.instance:
            TopicView.instance = TopicView(gSheet, embedFactory, data, title, currentPage, currentIndex, itemsPerPage)
        return TopicView.instance

    def refreshData(self):
        try:
            self._data = self._gSheet.refetchTopicData(self.title)
        except:
            raise Exception('GSpread API Error: Could not refresh spreadsheet data. ❌')
    
    def on_timeout(self) -> None:
        TopicView.instance = None
        TopicView.messageId = sys.maxsize