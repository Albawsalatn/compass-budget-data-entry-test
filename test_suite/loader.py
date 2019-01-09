import pygsheets


class Loader:
    def __init__(self, file_name=None):
        self.client = pygsheets.authorize(
            client_secret="credentials/client_secret.json",
            credentials_directory="credentials",
        )
        if file_name:
            self.load_data(file_name)
        else:
            self.load_data()

    def load_data(self, file_name="saisie_db"):
        """Downloads the specified Google Sheets document to the default directory.

        The class attribute `loaded_data` gets initialized in this function and can be
        accessed later on.
        
        Keyword Arguments:
            file_name {str} -- The file name of the Google Sheets document (default: {"saisie_db"})
        
        Returns:
        --------
        pygsheets.Spreadsheet
        """
        self.loaded_data = self.client.open(file_name)
        return self.load_data

    def worksheet_to_df(self, ws_name, *args, **kwargs):
        """Downloads the specified worksheet by its name into a Pandas DataFrame
        
        Arguments:
            ws_name {str} -- [description]
        
        Returns:
        --------
        pandas.DataFrame
        """
        sheet = self.loaded_data
        return sheet.worksheet_by_title(ws_name).get_as_df(*args, **kwargs)

