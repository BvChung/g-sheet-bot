import gspread
import config

Column_Headers = ['Number', 'Name', 'Category', 'Solution', 'Link', 'Review']
# newRow = [49, "Group Anagrams", "Arrays", "Use a hashmap with key: [the count of number of letters in the alphabet using ascii ord(curr char) - ord('a') indexed from 0-25] and value: [grouped anagrams]", 'https://leetcode.com/problems/group-anagrams/', 'no']

# print(leetcodeSheet.sheet1.delete_rows())
# print(leetcodeSheet.sheet1.insert_row(newRow, 2))
# leetcodeSheet.sheet1.sort((1, 'asc'))
# print(leetcodeSheet.sheet1.get_all_records())
# print(leetcodeSheet.sheet1.row_values(2))

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
    
    def createEntry(self, entries: list)->None:
        try:
            self.__leetcodeSheet.insert_row(entries, 2)
            self.__leetcodeSheet.sort((1, 'asc'))
        except:
            print('Unable to add new entry')