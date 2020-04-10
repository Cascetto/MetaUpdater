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

    def __init__(self, abs_path: str, filters=(".mp3", ".wav")):
        """
        Constructor
        :type abs_path: str
        the absolute path of the folder
        :type filters: str vector
        vector containing the desired extension
        """

        # append, if needed the '\' mark to the path
        if abs_path[len(abs_path) - 1] != '\\':
            abs_path += '\\'
        self.path = abs_path
        self.filters = filters
        self.sub_folders = []
        self.file_list = []
        self.update()
        print("Created")

    def update(self):
        for element in os.listdir(self.path):
            if os.path.isfile(self.path + element):
                # todo apply filter
                self.file_list.append(element)
            if os.path.isdir(self.path + element):
                self.sub_folders.append(element)
