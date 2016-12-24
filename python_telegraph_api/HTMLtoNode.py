from html.parser import HTMLParser

class neatHTMLParser(HTMLParser):
    def __init__(self):
    	HTMLParser.__init__(self)
    	self.nodes = []
    	self.iteratingListOfNodes, self.parentListOfNodes = self.nodes, []

    def handle_starttag(self, tag, attrs_list):
        node = {"tag":tag, "children":[]}

        if len(attrs_list)>0: 
            attrs={}
            for x,y in attrs_list: 
                attrs[x] = y
            node["attrs"] = attrs

        self.iteratingListOfNodes.append(node)
        self.parentListOfNodes.append(self.iteratingListOfNodes)

        self.iteratingListOfNodes = node['children']

    def handle_endtag(self, tag): 
    	self.iteratingListOfNodes = self.parentListOfNodes.pop(-1)

    def handle_data(self, data): 
    	self.iteratingListOfNodes.append(data)


def HTML_into_Node(content):
	parser = neatHTMLParser()
	parser.feed(content)
	return parser.nodes