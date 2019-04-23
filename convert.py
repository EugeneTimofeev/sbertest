import json


class JsonToHtml:

    def __init__(self):
        self.__json_data = ''
        self.__html_data = ''

    @property
    def json_data(self):
        return self.__json_data

    @json_data.setter
    def json_data(self, value):
        self.__json_data = value

    @property
    def html_data(self):
        return self.__html_data

    @html_data.setter
    def html_data(self, value):
        self.__html_data = value

    def load_json(self, file_name):
        with open(file_name, "r") as f:
            self.json_data = json.load(f)

    def json_to_html(self):
        if type(self.json_data) is list:
            self.html_data += '<ul>'
            for data in self.json_data:
                self.html_data += '<li>'
                for key in data:
                    self.html_data += '<' + key + '>' + data[key] + '</' + key + '>'
                self.html_data += '</li>'
            self.html_data += '</ul>'

    def save_html(self, file_name):
        with open(file_name, "w") as f:
            f.write(self.html_data)


if __name__ == '__main__':
    input_file = "source.json"
    output_file = "index.html"
    mydata = JsonToHtml()
    mydata.load_json(input_file)
    mydata.json_to_html()
    mydata.save_html(output_file)
