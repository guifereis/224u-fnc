from csv import DictReader
from tqdm import tqdm, trange

class DataSet():
    def __init__(self, name="train", path="fnc-1"):
        self.path = path

        print("Reading dataset")
        bodies = name+"_bodies.csv"
        stances = name+"_stances.csv"

        self.stances = self.read(stances)

        print("# stances before: "+str(len(self.stances)))
        #print(self.stances[0:5])
        #exit(0)
        new_stances = []
        for s_idx in trange(len(self.stances)):
            if self.stances[s_idx]["Stance"] != "unrelated":
                new_stances.append(self.stances[s_idx])
        self.stances = new_stances
        print("# stances AFTER: "+str(len(self.stances)))

        articles = self.read(bodies)
        self.articles = dict()

        #make the body ID an integer value
        for s in self.stances:
            s['Body ID'] = int(s['Body ID'])

        #copy all bodies into a dictionary
        for article in articles:
            self.articles[int(article['Body ID'])] = article['articleBody']

        print("Total stances: " + str(len(self.stances)))
        print("Total bodies: " + str(len(self.articles)))



    def read(self,filename):
        rows = []
        with open(self.path + "/" + filename, "r", encoding='utf-8') as table:
            r = DictReader(table)

            for line in r:
                rows.append(line)
        return rows
