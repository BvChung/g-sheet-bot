from .embeds import Embeds
from .pagination import PaginatedView
from .sheet import Sheet

class DefaultView(PaginatedView):
    def __init__(self, gSheet: Sheet, embedFactory: Embeds, data: list[dict], title:str, currentPage: int, currentIndex: int, itemsPerPage: int):
        super().__init__(gSheet, embedFactory, data, title, currentPage, currentIndex, itemsPerPage)
    
    def refreshData(self):
        self.data = self.gSheet.refetchAllData()