import gspread
import config

# Column_Headers = ['Number', 'Name', 'Category', 'Solution', 'Link', 'Review']
# newR = [[1, "Group Anagrams", "Arrays", "Use a", "link", 'no']]
# newRow = [49, "Group Anagrams", "Arrays", "Use a hashmap with key: [the count of number of letters in the alphabet using ascii ord(curr char) - ord('a') indexed from 0-25] and value: [grouped anagrams]", 'https://leetcode.com/problems/group-anagrams/', 'no']

class Sheet:
    instance = None

    def __init__(self, credentials, sheetName) -> None:
        self.__leetcodeSheet = gspread.service_account_from_dict(credentials).open(sheetName).sheet1
        self.__cachedData: list[dict] = []
        self.__cachedCategoryData: list[dict] = []
    
    @staticmethod
    def getState():
        if not Sheet.instance:
            Sheet.instance = Sheet(config.credentials, config.sheetName)
        return Sheet.instance
    
    def __fetch(self)->None:
        self.__cachedData = self.__leetcodeSheet.get_all_records()

    def __filter(self, category:str)->list[dict]:
        filteredData :list[dict] = []
        for row in self.__cachedData:
            if row['Category'].lower() == category.lower():
                filteredData.append(row)

        self.__cachedCategoryData = filteredData
        return self.__cachedCategoryData
    
    def __find(self, problemNumber: str):
        return self.__leetcodeSheet.find(problemNumber)
    
    def getAllData(self)->list[dict]:
        if not self.__cachedData:
            self.__fetch()
        return self.__cachedData

    def filterByCategory(self, category: str)->list[dict]:
        if not self.__cachedCategoryData:
            self.__fetch()
        return self.__filter(category)

    def refetchAllData(self)->list[dict]:
        self.__fetch()
        return self.__cachedData
    
    def refetchCategoryData(self, category: str)->list[dict]:
        self.__fetch()
        return self.__filter(category)
    
    def createEntry(self, entries: list)->bool:
        try:
            self.__leetcodeSheet.insert_row(entries, 2)
            self.__leetcodeSheet.sort((1, 'asc'))
            return True
        except:
            print('Unable to create new entry')
            return False
    
    def getEntry(self, problemNumber: int):
        cell = self.__find(str(problemNumber))

        if not cell:
            return None
        
        rowNumber: int = cell.row
        return [rowNumber, self.__leetcodeSheet.row_values(cell.row)]
        
    def updateEntry(self, rowNumber: int, updatedData: list)->bool:
        cellRange = f'A{str(rowNumber)}:F{str(rowNumber)}' 
        try:
            self.__leetcodeSheet.update(cellRange, updatedData) 
            return True
        except:
            print(f'Could not update row #{rowNumber}.')
            return False
    
    def deleteEntry(self, problemNumber: int)->bool:
        cell = self.__find(str(problemNumber))

        if not cell:
            return False
        
        try:
            self.__leetcodeSheet.delete_rows(int(cell.row))
            return True
        except:
            print(f'Could not delete row #{cell.row}')
            return False