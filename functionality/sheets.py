import gspread
import config

class GSheet:
    instance = None

    def __init__(self, credentials, sheetName) -> None:
        self.leetcodeSheet = gspread.service_account_from_dict(credentials).open(sheetName)
    
    @staticmethod
    def getGSheetState():
        if not GSheet.instance:
            GSheet.instance = GSheet(config.credentials, config.sheetName)
        return GSheet.instance