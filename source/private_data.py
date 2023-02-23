import yaml

class Private(dict):
    def __init__(self,filelocation,*arg,**kw):
        super(Private, self).__init__(*arg, **kw)
        self.filelocation = filelocation
        self.load_data()
        
    
    def load_data(self):
        with open(self.filelocation, 'r', encoding='utf-8') as f:
            private_data = yaml.safe_load(f)
            for key in private_data:
                print(private_data[key])
                self[key] = private_data[key]
        
        


        