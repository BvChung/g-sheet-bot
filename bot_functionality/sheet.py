import gspread

class Sheet:
    instance = None
    
    def __init__(self, credentials: dict, sheet_name: str, starting_column: str, ending_column: str) -> None:
        self.__leetcode_sheet = gspread.service_account_from_dict(credentials).open(sheet_name).sheet1
        self.__cached_data: list[dict] = []
        self.__cached_topic_data: list[dict] = []
        self.starting_column = starting_column
        self.ending_column = ending_column
    
    @staticmethod
    def get_state(credentials: dict, sheet_name: str, starting_column: str, ending_column: str):
        if not Sheet.instance:
            Sheet.instance = Sheet(credentials, sheet_name, starting_column, ending_column)
        return Sheet.instance
    
    def __fetch(self) -> None:
        try:
            self.__cached_data = self.__leetcode_sheet.get_all_records()
        except Exception as error:
            raise Exception(f'Unable to fetch spreadsheet data. ❌\n{error}')

    def __filter(self, topic:str) -> list[dict]:
        filtered_data :list[dict] = []
        for row in self.__cached_data:
            if row['Topic'].lower() == topic.lower():
                filtered_data.append(row)

        self.__cached_topic_data = filtered_data
        return self.__cached_topic_data
    
    def __find(self, problem_number: str):
        cell = self.__leetcode_sheet.find(problem_number)
        
        if not cell:
            raise Exception(f'Problem #{problem_number} could not be found.')
        
        return cell
    
    def get_all_data(self) -> list[dict]:
        if not self.__cached_data:
            self.__fetch()
        return self.__cached_data

    def filter_by_topic(self, topic: str) -> list[dict]:
        if not self.__cached_topic_data:
            self.__fetch()
        return self.__filter(topic)

    def refetch_all_data(self) -> list[dict]:
        self.__fetch()
        return self.__cached_data
    
    def refetch_topic_data(self, topic: str) -> list[dict]:
        self.__fetch()
        return self.__filter(topic)
    
    def create_entry(self, entries: list) -> None:
        try:
            self.__leetcode_sheet.insert_row(entries, 2)
            self.__leetcode_sheet.sort((1, 'asc'))
        except Exception as error:
            raise Exception(f'Unable to create new entry.\n{error}')
    
    def get_entry(self, problem_number: int):
        cell = self.__find(str(problem_number))

        row_number: int = cell.row
        return [row_number, self.__leetcode_sheet.row_values(cell.row)]
        
    def update_entry(self, row_number: int, updated_data: list) -> None:
        cell_range = f'{self.starting_column}{str(row_number)}:{self.ending_column}{str(row_number)}' 
        try:
            self.__leetcode_sheet.update(cell_range, updated_data) 
        except Exception as error:
            print(error)
            raise Exception(f'Could not update entry.\n{error}.')
    
    def delete_entry(self, problem_number: int) -> None:
        cell = self.__find(str(problem_number))
        
        try:
            self.__leetcode_sheet.delete_rows(int(cell.row))
        except Exception as error:
            print(error)
            raise Exception(f'Could not delete entry.\n{error}')