class pnode:
    def __init__(self,data,pnext=None):
        self.data=data
        self.next=pnext

    def __repr__(self):
        return str(self.data)

    def isEmpty(self):
        return (self.length==0)
    
