class textAlert:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    def header(self,message):
        print self.HEADER+message
    def okblue(self,message):
        print self.OKBLUE+message
    def okgreen(self,message):
        print self.OKGREEN+message
    def warning(self,message):
        print self.WARNING+message
    def fail(self,message):
        print self.FAIL+message
    def endc(self,message):
        print self.ENDC+message
