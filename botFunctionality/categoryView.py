from .embeds import Embeds
from .pagination import PaginatedView
from .sheet import Sheet

class CategoryView(PaginatedView):
    instance = None
    def __init__(self, gSheet: Sheet, embedFactory: Embeds, data: list[dict], title:str, currentPage: int, currentIndex: int, itemsPerPage: int):
        super().__init__(gSheet, embedFactory, data, title, currentPage, currentIndex, itemsPerPage)

    @staticmethod
    def getState(gSheet: Sheet, embedFactory: Embeds, data: list[dict], title:str, currentPage: int, currentIndex: int, itemsPerPage: int):
        if not CategoryView.instance:
            CategoryView.instance = CategoryView(gSheet, embedFactory, data, title, currentPage, currentIndex, itemsPerPage)
        return CategoryView.instance

    def refreshData(self):
        self._data = self._gSheet.refetchCategoryData(self.title)
    
    def on_timeout(self) -> None:
        print('Category timeout')
        CategoryView.instance = None