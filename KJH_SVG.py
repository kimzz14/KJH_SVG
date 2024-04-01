class element:
    def __init__(self,name, container):
        self.name = name
        self.attr_DICT = {}
        self.attrKey_LIST = []
        self.style_DICT = {}
        self.styleKey_LIST = []
        self.item_LIST = []

        if container != None:
            container.add(self)
        self.default()
    def default(self):
        self.style('box-sizing', 'border-box')
        self.style('float', 'left')
        self.style('font-family', 'Times New Roman')

    def add(self,item):
        self.item_LIST += [item]
    def __getitem__(self,key):
        return self.attr_DICT[key]
    def attr(self,key,value):
        if key in self.attr_DICT:
            self.attr_DICT[key] = value
        else:
            self.attr_DICT[key] = value
            self.attrKey_LIST += [key]
        return self
    def style(self,key,value):
        if key in self.style_DICT:
            self.style_DICT[key] = value
        else:
            self.style_DICT[key] = value
            self.styleKey_LIST += [key]
        return self
    def __repr__(self):
        tag = '<'+ self.name
        for attrKey in self.attrKey_LIST:
            tag += ' ' + attrKey + '=' + '"' + str(self.attr_DICT[attrKey]) + '"'
        style = ''
        for styleKey in self.styleKey_LIST:
            style += styleKey + ':' + str(self.style_DICT[styleKey]) + ';'
        if style != '':
            tag += ' ' + 'style' + '=' + '"'  + style + '"'
        tag += '>'

        for item in self.item_LIST:
            tag += str(item)
        tag += '</' + self.name + '>'
        return tag