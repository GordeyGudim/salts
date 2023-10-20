import separation
class Salt():
    def __init__(self, form):
        self.strong_metal = ['Na', 'Li', 'K', 'Rb', 'Cs', 'Ca', 'Sn', 'Ba']
        self.acid_residue = ['Cl', 'SO4', 'NO3', 'Br', 'I', 'CLO3', 'CLO4']
        self.form = form
    def analysis(self, result_1=0, result_2=0):
        for metal in self.strong_metal:
            if metal in self.form:
                result_1 += 1
        for acid in self.acid_residue:
            if acid in self.form:
                result_2 += 1
        return result_1, result_2
    def results(self):
        if self.analysis()[0] == 1:
            if self.analysis()[1] == 1:
                print('сил.м + сил.ост')
            else:
                print('сил.м + сл.ост')
        else:
            if self.analysis()[1] == 1:
                print('сл.м + сил.ост')
            else:
                print('сл.м + сл.ост')
my_salt = Salt('CuCl')
my_salt.results()

        