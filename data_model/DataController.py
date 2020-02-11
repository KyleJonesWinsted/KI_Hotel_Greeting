import json
from data_model.Template import Template


class DataController(object):

    def __init__(self):
        self.file_paths = {}

    def add_file_path(self, path_name, file_path):
        self.file_paths[path_name] = file_path

    def _get_file_path(self, path_name):
        try:
            file_path = self.file_paths[path_name]
            return file_path
        except:
            raise FileException("No file path for {}".format(path_name))

    def get_template_names(self):
        file_path = self._get_file_path('templates')
        names = []
        with open(file_path) as json_file:
            data = json.load(json_file)
            for template in data:
                names.append({template['id'], template['shortName']})
        return names

    def get_template_by_id(self, id):
        file_path = self._get_file_path('templates')
        template_json = {}
        with open(file_path) as json_file:
            data = json.load(json_file)
            template_json = next((t for t in data if t['id'] == id), None)
        if template_json:
            template = Template(template_json['shortName'], template_json['templateText'])
        else:
            return None
        return template
        


class FileException(Exception):
    pass