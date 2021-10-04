# Testing a class for creating KMap (Karnaugh map) rendering in latex

class Kmap:
    def __init__(self, greycode:list = ["00", "01", "11", "10"], columns:list = ["x", "y"], rows:list = ["z"]):
        self.greycode = greycode
        self.columns = columns
        self.rows = rows
        self.kmap = []

    def two_input(self):
        self.kmap.append(["0","1"])

    def three_input(self):
        self.kmap.append(self.greycode)
    
    def four_input(self):
        self.kmap.append(self.greycode)

    def __repr__(self):
        result = f"""
        {self.columns[0]} {self.columns[1] if len(self.columns) == 2 else ''} \t {'    '.join(self.greycode) if len(self.columns) == 2 else '0    1'}
        {self.rows[0]} {self.rows[1] if len(self.rows) == 2 else ''} 
        """
        return result 




# if __name__ == "__main__":
#     k = Kmap()
#     k.three_input()
#     print(k)