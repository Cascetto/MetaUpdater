import os


class FolderParser:
    """
    Parse the content of a folder [if required even the subfolders] given in the constructor,
    applying the selected filter (default (".mp3", ".wav"), can be none [=""])
    :var path: the absolute path of the folder
    :var filter: the tuple of filters
    :var sub_folders: the list of subfolders
    :var file_list: the list of files
    """

    def __init__(self, abs_path: str, filters: tuple = (".mp3", ".wav")):
        """
        Constructor
        :type abs_path: str
        the absolute path of the folder
        :type filters: str vector
        vector containing the desired extension
        """

        # append, if needed, the '\' mark to the path
        if abs_path[len(abs_path) - 1] != '\\':
            abs_path += '\\'
        self.path = abs_path
        # if there is only one filter, convert it to tuple
        if not isinstance(filters, tuple):
            filters = (filters,)
        self.filters = filters
        self.sub_folders = []
        self.file_list = []
        self.update()
        print("\nCreated\n" + self.path)

    @staticmethod
    def get_extension(file_name: str) -> str:
        """
        static method
        :return the extension of a given file (if missing, return '.error')
        """
        result = ".error"
        separator = file_name.rfind(".")
        if separator != -1:
            result = file_name[separator: len(file_name)]
        return result

    def update(self):
        """
        update the list of subfolders and files in the instance,
        called in the constructor and, eventually, whens a filesystem event occur
        :return:
        """
        for element in os.listdir(self.path):
            if os.path.isfile(self.path + element):
                filter_match = False
                # get the file extension
                ext = FolderParser.get_extension(element)
                # check for match with the filter
                for f in self.filters:
                    if ext == f:
                        filter_match = True
                        break
                # if the file has correct extension, add to the file list
                if filter_match:
                    self.file_list.append(element)
            if os.path.isdir(self.path + element):
                self.sub_folders.append(element)

    def get_all_file_names(self) -> list or None:
        """
        recursive function, call itself in the subfolders instance
        :return a list of all files (including the one in subfolders):
        """
        result = self.file_list
        for sub_folder in self.sub_folders:
            # get the files in subfloders
            sub_list = FolderParser(self.path + sub_folder, self.filters).get_all_file_names()
            if len(sub_list) > 0:
                result += sub_list
        return result
