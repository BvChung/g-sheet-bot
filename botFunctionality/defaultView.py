from .embeds import Embeds
from .pagination import PaginatedView
from .sheet import Sheet

class DefaultView(PaginatedView):
    instance = None
    def __init__(self, gSheet: Sheet, embedFactory: Embeds, data: list[dict], title:str, currentPage: int, currentIndex: int, itemsPerPage: int):
        super().__init__(gSheet, embedFactory, data, title, currentPage, currentIndex, itemsPerPage)
    
    @staticmethod
    def getState(gSheet: Sheet, embedFactory: Embeds, data: list[dict], title:str, currentPage: int, currentIndex: int, itemsPerPage: int):
        if not DefaultView.instance:
            DefaultView.instance = DefaultView(gSheet, embedFactory, data, title, currentPage, currentIndex, itemsPerPage)
            return DefaultView.instance
        return DefaultView.instance

    def refreshData(self):
        self.data = self.gSheet.refetchAllData()
          
    def on_timeout(self) -> None:
        print('Default timeout')
        DefaultView.instance = None