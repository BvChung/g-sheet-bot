import gspread
from gspread import Worksheet
from gspread.utils import ValueRenderOption


class GSheetInstance:
    def __init__(self, credentials_filename: str, spreadsheet_key: str, worksheet_gid: int | None = None) -> None:
        self.__spreadsheet_key = spreadsheet_key
        self.__connection = gspread.service_account(
            credentials_filename)
        self.__spreadsheet = self.__connection.open_by_key(
            spreadsheet_key)

        if not worksheet_gid:
            self.__active_worksheet = self.__spreadsheet.sheet1
        else:
            self.__active_worksheet = self.__spreadsheet.get_worksheet_by_id(
                worksheet_gid)

        self.worksheet_gid = self.__active_worksheet.id

    def set_spreadsheet_key(self, spreadsheet_key: str, worksheet_gid: int = 0) -> None:
        """
        Spreadsheet key is the unique identifier for a google spreadsheet located in the url between d/ and /edit.
        """
        if self.__spreadsheet_key == spreadsheet_key:
            return

        self.worksheet_gid = worksheet_gid
        self.__spreadsheet_key = spreadsheet_key

        self.__spreadsheet = self.__connection.open_by_key(
            spreadsheet_key)
        self.__active_worksheet = self.__spreadsheet.get_worksheet_by_id(
            self.worksheet_gid)

    def set_worksheet_gid(self, worksheet_gid: int) -> None:
        """
        Spreadsheet id is located in the url of the spreadsheet in the browser indicated by the gid= parameter.
        """
        if self.worksheet_gid == worksheet_gid:
            return

        self.worksheet_gid = worksheet_gid
        self.__active_worksheet = self.__connection.open_by_key(
            self.__spreadsheet_key).get_worksheet_by_id(self.worksheet_gid)

    def get_all_rows(self) -> list:

        return self.__active_worksheet.get_values(
            value_render_option=ValueRenderOption.unformatted)

    def get_all_sheets(self) -> list[Worksheet]:
        return self.__active_worksheet.spreadsheet.worksheets()

    def get_spreadsheet_filename(self) -> str:
        return self.__spreadsheet.title

    def get_child_spreadsheet_name(self) -> str:
        return self.__active_worksheet.title

    def get_id_identifier(self) -> str:
        return f'{self.__spreadsheet_key}_{self.worksheet_gid}'
