import json
import html


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

        for data in self.json_data:
            self.html_data += '<'
            tag = data[:data.find('.')]
            self.html_data += tag + ' '
            attr = data[data.find('.') + 1:]
            if attr.find('#') != -1:
                id = attr[attr.find('#') + 1:]
                attr = attr[:attr.find('#')]
            else:
                id = ''
            classes = attr.replace('.', ' ')
            if id:
                self.html_data += 'id="' + id + '" '
            self.html_data += 'class="' + classes + '">' + html.escape(self.json_data[data],
                                                                       quote=True) + '</' + tag + '>'

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
