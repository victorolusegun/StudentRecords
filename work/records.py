class StudentRecords:
    def __init__(self):
        self.records = {}
    
    def add_student(self, name, std_score):
        self.records[name] = std_score
    
    def view_student(self):
        if len(self.records) != 0:
            for index, (key, values) in enumerate(self.records.items(), start = 1):
                print(f'{index}. {key} : {values}')
        else:
            print('No available records to view.')
    def update_student(self, name, new_score):
        if len(self.records) == 0:
            print('No record to update.')
        elif name in self.records:
            self.records[name] = new_score
        else:
            print(f'Student {name} not found in records.')


class Statistics():
    def __init__(self, scores):
       self.scores = scores
    
    def num_std(self):
       num = len(self.scores)
       return num
    
    def max_score(self):
        high_score = max(self.scores)
        return high_score
     
    def min_score(self):
        low_score = min(self.scores)
        return low_score
    
    def avg_score(self):
        sum_score = sum(self.scores)
        num = len(self.scores)
        avg = sum_score / num
        return avg