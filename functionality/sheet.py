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
        self.leetcodeSheet = gspread.service_account_from_dict(credentials).open(sheetName).sheet1
        self.cacheData = []
    
    @staticmethod
    def getSheetState():
        if not Sheet.instance:
            Sheet.instance = Sheet(config.credentials, config.sheetName)
        return Sheet.instance
    
    def getAllData(self)->list[dict]:
        return self.leetcodeSheet.get_all_records()

    def filterByCategory(self, category: str):
        data = self.getAllData()
        filteredData :list[dict] = []
        for row in data:
            if row['Category'].lower() == category.lower():
                filteredData.append(row)

        return filteredData

    def createEntry(self, entries: list):
        try:
            self.leetcodeSheet.insert_row(entries, 2)
            self.leetcodeSheet.sort((1, 'asc'))
        except:
            print('Unable to add new entry')
    
    def sortSheet(self):
        try:
            newRow = [69, "Group Anagrams", "Arrays", "Use a hashmap with key: [the count of number of letters in the alphabet using ascii ord(curr char) - ord('a') indexed from 0-25] and value: [grouped anagrams]", 'https://leetcode.com/problems/group-anagrams/', 'no']

            self.leetcodeSheet.insert_row(newRow, 2)
            self.leetcodeSheet.sort((1, 'asc'))
        except:
            print('Could not sort sheet')