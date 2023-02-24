from .embeds import Embeds
from .pagination import PaginatedView
from .sheet import Sheet

class CategoryView(PaginatedView):
    def __init__(self, gSheet: Sheet, embedFactory: Embeds, data: list[dict], title:str, currentPage: int, currentIndex: int, itemsPerPage: int, category: str):
        super().__init__(gSheet, embedFactory, data, title, currentPage, currentIndex, itemsPerPage)
        self.category = category

    def refreshData(self):
        self.data = self.gSheet.refetchCategoryData(self.category)