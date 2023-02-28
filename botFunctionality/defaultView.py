import sys
from .embeds import Embeds
from .pagination import PaginatedView
from .sheet import Sheet

class DefaultView(PaginatedView):
    instance = None
    messageId: int = sys.maxsize

    def __init__(self, gSheet: Sheet, embedFactory: Embeds, data: list[dict], title:str, currentPage: int, currentIndex: int, itemsPerPage: int):
        super().__init__(gSheet, embedFactory, data, title, currentPage, currentIndex, itemsPerPage)
    
    @staticmethod
    def getState(gSheet: Sheet, embedFactory: Embeds, data: list[dict], title:str, currentPage: int, currentIndex: int, itemsPerPage: int):
        if not DefaultView.instance:
            DefaultView.instance = DefaultView(gSheet, embedFactory, data, title, currentPage, currentIndex, itemsPerPage)
        return DefaultView.instance

    def refreshData(self):
        try:
            self._data = self._gSheet.refetchAllData()
        except:
            raise Exception('GSpread API Error: Could not refresh spreadsheet data. ❌')
          
    def on_timeout(self) -> None:
        DefaultView.instance = None
        DefaultView.messageId = sys.maxsize