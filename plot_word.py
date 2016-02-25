import matplotlib.pyplot as plt 
def plot_frequency():
    data = []
    with open('./plotable1001') as f:
        lines = f.read().splitlines()
        for i in range(len(lines)):
            data.append(tuple(lines[i]))
        print lines
    # plt.plot(*zip(*data))
    # plt.show()

def tuple_to_int(tup1, tup2 =0):
    return tuple(int(tup1[0]), int(tup1[1]))

def to_int(inp):
    # print inp, type(inp)
    return int(inp[0]), int(inp[1])

def plot_frequency2():
    data = [to_int(tuple(line.strip().split(' ',1))) for line in open ('./plotable1001')]
    print data
    plt.plot(*zip(*data))
    plt.show()
# plot_frequency2()


def strip_common():
    with open('./1000onlywords') as f:
        data = f.read().splitlines()
        common = ['all', 'just', 'being', 'over', 'both', 'through', 'yourselves', 'its', 'before', 'herself', 'had', 'should', 'to', 'only', 'under', 'ours', 'has', 'do', 'them', 'his', 'very', 'they', 'not', 'during', 'now', 'him', 'nor', 'did', 'this', 'she', 'each', 'further', 'where', 'few', 'because', 'doing', 'some', 'are', 'our', 'ourselves', 'out', 'what', 'for', 'while', 'does', 'above', 'between', 't', 'be', 'we', 'who', 'were', 'here', 'hers', 'by', 'on', 'about', 'of', 'against', 's', 'or', 'own', 'into', 'yourself', 'down', 'your', 'from', 'her', 'their', 'there', 'been', 'whom', 'too', 'themselves', 'was', 'until', 'more', 'himself', 'that', 'but', 'don', 'with', 'than', 'those', 'he', 'me', 'myself', 'these', 'up', 'will', 'below', 'can', 'theirs', 'my', 'and', 'then', 'is', 'am', 'it', 'an', 'as', 'itself', 'at', 'have', 'in', 'any', 'if', 'again', 'no', 'when', 'same', 'how', 'other', 'which', 'you', 'after', 'most', 'such', 'why', 'a', 'off', 'i', 'yours', 'so', 'the', 'having', 'once']
        s = set(common)
        cleandata = [x for x in data if x not in s]
        for i in range(50):
            print cleandata[i] + ', '
strip_common()
