class StudentRecords:
    def __init__(self):
        self.records = {}
    
    def add_student(self, name, std_score):
        self.records[name] = std_score
    