arunFruits = {'apples':1,'bananas':12,'pears':7}
bethFruits = {'pears':8,'apples':3,'cherries':6}
choFruits = {}
def combine(d1, d2):
    dSum = {}
    for key in d1:
        if key in d2:
            dSum[key]=d1.get(key)+d2.get(key)
        else:
            dSum[key]=d1.get(key)
    for key1 in d2:
        if key1 in d1:
            dSum[key1]=d1.get(key1)+d2.get(key1)
        else:
            dSum[key1]=d2.get(key1)
    return dSum
