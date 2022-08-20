# This is a test for H5.
import random
import copy
import time
from H5 import TreeNode, mydict


def check(dic1, dic2):
    try:
        for item in dic1:
            assert item in dic2, print(item, 1)
        for item in dic2:
            assert item in dic1, print(item, 2)
    except AssertionError as e:
        return False
    return True

# 进入测试前请保证实现了__str__()且__contains__()不能出错


char = [chr(i) for i in range(ord('a'), ord('z') + 1)]


def setTest():
    dic1 = mydict()
    dic2 = dict()
    lst1 = [i for i in range(100000)]
    random.shuffle(lst1)
    lst1 = lst1[:1000]
    for item in lst1:  # 非负整数赋值
        dic1[item] = item
        dic2[item] = item
    assert check(dic1, dic2), "test point 1-1 break\nlst={}\ndic1={}\ndic2={}".format(lst1, dic1, dic2)
    for item in lst1:  # 负整数赋值
        dic1[-item] = -item
        dic2[-item] = -item
    assert check(dic1, dic2), "test point 1-2 break\nlst={}\ndic1={}\ndic2={}".format(lst1, dic1, dic2)
    lst2 = [random.uniform(1, 100000) for i in range(50)]
    for item in lst2:  # 浮点数赋值
        dic1[item] = item
        dic2[item] = item
    assert check(dic1, dic2), "test point 1-3 break\nlst={}\ndic1={}\ndic2={}".format(lst1 + lst2, dic1, dic2)
    lst3 = [''.join([random.choice(char) for i in range(random.randint(0, 100))]) for j in range(50)]
    for item in lst3:  # 字符串赋值
        dic1[item] = item
        dic2[item] = item
    assert check(dic1, dic2), "test point 1-4 break\nlst={}\ndic1={}\ndic2={}".format(lst1 + lst2 + lst3, dic1, dic2)
    for item in lst1:  # 更改值
        dic1[item] = item
        dic2[item] = item
    assert check(dic1, dic2), "test point 1-5 break\nlst={}\ndic1={}\ndic2={}".format(lst1 + lst2 + lst3, dic1, dic2)

    print("set test pass.")


def getTest():
    dic1 = mydict()
    dic2 = dict()
    lst1 = [i for i in range(100000)]
    random.shuffle(lst1)
    lst1 = lst1[:5000]
    for item in lst1:
        dic1[item] = item
        dic2[item] = item
    getList = copy.copy(lst1)
    random.shuffle(getList)
    getList = getList[:1000]
    for item in getList:  # 获取值
        assert dic1[item] == dic2[item], "test point 2-1 break\nlst={}\nitem={}\ndic1={}\ndic2={}".format(lst1, item, dic1, dic2)
    assert check(dic1, dic2), "test point 2-1 break\nlst={}\ngetList={}\ndic1={}\ndic2={}".format(lst1, getList, dic1, dic2)
    unfillList = [i for i in range(200000, 200100)]  # 未赋过的键
    for item in unfillList:  # 获取未赋过的键值
        try:
            dic1[item]
        except KeyError:
            pass
        else:
            assert False, "test point 2-2 break\nlst={}\ngetList={}\nitem={}\ndic1={}\ndic2={}".format(lst1, getList, item, dic1, dic2)
    assert check(dic1, dic2), "test point 2-2 break\nlst={}\ngetList={}\nunfillList={}\ndic1={}\ndic2={}".format(lst1, getList, unfillList, dic1, dic2)
    for item in lst1:  # 更改值后获取值
        dic1[item] = -item
        dic2[item] = -item
    for item in getList:
        assert dic1[item] == dic2[item], "test point 2-3 break\nlst={}\nitem={}\ndic1={}\ndic2={}".format(lst1, item, dic1, dic2)
    assert check(dic1, dic2), "test point 2-3 break\nlst={}\ngetList={}\ndic1={}\ndic2={}".format(lst1, getList, dic1, dic2)

    print("get test pass.")


def delTest():
    dic1 = mydict()
    dic2 = dict()
    lst1 = [i for i in range(100000)]
    random.shuffle(lst1)
    lst1 = lst1[:5000]
    delList = copy.copy(lst1)
    random.shuffle(delList)
    delList = delList[:1000]
    for item in lst1:
        dic1[item] = item
        dic2[item] = item
    for item in delList:  # 删除键值
        del dic1[item]
        del dic2[item]
    assert check(dic1, dic2), "test point 3-1 break\nlst={}\ndelList={}\ndic1={}\ndic2={}".format(lst1, delList, dic1, dic2)
    for item in delList:  # 获取删除后的键值
        try:
            dic1[item]
        except KeyError:
            pass
        else:
            assert False, "test point 3-2 break\nlst={}\nitem={}\ndic1={}\ndic2={}".format(lst1, item, dic1, dic2)
    assert check(dic1, dic2), "test point 3-2 break\nlst = {}\ndelList={}\ndic1={}\ndic2={}".format(lst1, delList, dic1, dic2)
    for item in delList:  # 删除删除后的键值
        try:
            del dic1[item]
        except KeyError:
            pass
        else:
            assert False, "test point 3-3 break\nlst={}\nitem={}\ndic1={}\ndic2={}".format(lst1, item, dic1, dic2)
    assert check(dic1, dic2), "test point 3-3 break\nlst={}\ndelList={}\ndic1={}\ndic2={}".format(lst1, delList, dic1, dic2)
    unfillList = [i for i in range(200000, 200100)]  # 未赋过的键
    for item in unfillList:  # 删除未赋过的键
        try:
            del dic1[item]
        except KeyError:
            pass
        else:
            assert False, "test point 3-4 break\nlst={}\ndelList={}\nitem={}\ndic1={}\ndic2={}".format(lst1, delList, item, dic1, dic2)
    assert check(dic1, dic2), "test point 3-4 break\nlst={}\ndelList={}\ndic1={}\ndic2={}".format(lst1, delList, dic1, dic2)
    print("del test pass.")


def basicTest():
    dic1 = mydict()
    assert len(dic1) == 0, "test point 4-1 break"
    lst1 = [i for i in range(1000)]
    random.shuffle(lst1)
    lst1 = lst1[:500]
    for item in lst1:
        dic1[item] = item
    assert len(dic1) == len(lst1), "test point 4-2 break\nlst={}\ndic1={}\nlength={}".format(lst1, dic1, len(dic1))
    delList = copy.copy(lst1)
    random.shuffle(delList)
    delList = delList[:100]
    for item in delList:
        del dic1[item]
    assert len(dic1) == len(lst1) - len(delList), "test point 4-3 break\nlst={}\ndelList={}\ndic1={}\nlength={}".format(lst1, delList, dic1, len(dic1))
    for item in delList:
        dic1[item] = item
    assert dic1.keys() == sorted(lst1), "test point 4-4 break\nlst={}\ndic1={}\nkeys={}".format(lst1, dic1, dic1.keys())
    assert dic1.values() == sorted(lst1), "test point 4-5 break\nlst={}\ndic1={}\nkeys={}".format(lst1, dic1, dic1.values())
    alst = []
    for item in dic1:  # iter
        alst.append(item)
    assert alst == sorted(lst1), "test point 4-6 break\nlst={}\ndic1={}\niter={}".format(lst1, dic1, alst)
    blst = []
    clst = []
    for i in dic1:  # 多iter
        for j in dic1:
            blst.append((i, j))
    for i in sorted(lst1):
        for j in sorted(lst1):
            clst.append((i, j))
    assert blst == clst, "test point 4-7 break\nlst={}\ndic1={}\niter={}".format(lst1, dic1, blst)
    dic1.clear()
    assert len(dic1) == 0, "test point 4-8 break\ndic1={}\nlength={}".format(dic1, len(dic1))

    print("basic test pass.")


def hashCrackTest():
    dic1 = mydict()
    dic2 = dict()
    lst1 = [(2 ** 61 - 1) * i for i in range(1000)]
    random.shuffle(lst1)
    lst1 = lst1[:500]
    for item in lst1:  # 哈希冲突整数赋值
        dic1[item] = item
        dic2[item] = item
    assert check(dic1, dic2), "test point 5-1 break\nlst={}\ndic1={}\ndic2={}".format(lst1, dic1, dic2)
    getList = copy.copy(lst1)
    getList = getList[:100]
    for item in getList:  # 获取值
        assert dic1[item] == dic2[item], "test point 5-2 break\nlst={}\nitem={}\ndic1={}\ndic2={}".format(lst1, item, dic1, dic2)
    assert check(dic1, dic2), "test point 5-2 break\nlst={}\ngetList={}\ndic1={}\ndic2={}".format(lst1, getList, dic1, dic2)
    unfillList = [(2 ** 61 - 1) * i for i in range(200000, 200100)]  # 未赋过的键
    for item in unfillList:  # 获取未赋过的键值
        try:
            dic1[item]
        except KeyError:
            pass
        else:
            assert False, "test point 5-3 break\nlst={}\ngetList={}\nitem={}\ndic1={}\ndic2={}".format(lst1, getList, item, dic1, dic2)
    assert check(dic1, dic2), "test point 5-3 break\nlst={}\ngetList={}\nunfillList={}\ndic1={}\ndic2={}".format(lst1, getList, unfillList, dic1, dic2)
    for item in lst1:  # 更改值后获取值
        dic1[item] = -item
        dic2[item] = -item
    for item in getList:
        assert dic1[item] == dic2[item], "test point 5-4 break\nlst={}\nitem={}\ndic1={}\ndic2={}".format(lst1, item, dic1, dic2)
    assert check(dic1, dic2), "test point 5-4 break\nlst={}\ngetList={}\ndic1={}\ndic2={}".format(lst1, getList, dic1, dic2)
    delList = copy.copy(lst1)
    random.shuffle(delList)
    delList = delList[:100]
    for item in lst1:
        dic1[item] = item
        dic2[item] = item
    for item in delList:  # 删除键值
        del dic1[item]
        del dic2[item]
    assert check(dic1, dic2), "test point 5-5 break\nlst={}\ndelList={}\ndic1={}\ndic2={}".format(lst1, delList, dic1, dic2)
    for item in delList:  # 获取删除后的键值
        try:
            dic1[item]
        except KeyError:
            pass
        else:
            assert False, "test point 5-6 break\nlst={}\nitem={}\ndic1={}\ndic2={}".format(lst1, item, dic1, dic2)
    assert check(dic1, dic2), "test point 5-6 break\nlst = {}\ndelList={}\ndic1={}\ndic2={}".format(lst1, delList, dic1, dic2)
    for item in delList:  # 删除删除后的键值
        try:
            del dic1[item]
        except KeyError:
            pass
        else:
            assert False, "test point 5-7 break\nlst={}\nitem={}\ndic1={}\ndic2={}".format(lst1, item, dic1, dic2)
    assert check(dic1, dic2), "test point 5-7 break\nlst={}\ndelList={}\ndic1={}\ndic2={}".format(lst1, delList, dic1, dic2)
    unfillList = [(2 ** 61 - 1) * i for i in range(2000, 2100)]  # 未赋过的键
    for item in unfillList:  # 删除未赋过的键
        try:
            del dic1[item]
        except KeyError:
            pass
        else:
            assert False, "test point 5-8 break\nlst={}\ndelList={}\nitem={}\ndic1={}\ndic2={}".format(lst1, delList, item, dic1, dic2)
    assert check(dic1, dic2), "test point 5-8 break\nlst={}\ndelList={}\ndic1={}\ndic2={}".format(lst1, delList, dic1, dic2)

    print("hash crack test pass.")


def performanceTest():
    dic1 = mydict()
    dic2 = dict()
    lst1 = [i for i in range(100000)]
    t_beg = time.time()
    for item in lst1:
        dic1[item] = None
    for item in lst1:
        del dic1[item]
    t_end = time.time()
    print("mydict: {:.3f}s".format(t_end-t_beg))
    t_beg = time.time()
    for item in lst1:
        dic2[item] = None
    for item in lst1:
        del dic2[item]
    t_end = time.time()
    print("dict: {:.3f}s".format(t_end-t_beg))


def getHeight(Node):
    if Node is None:
        return 0
    else:  # 递归计算子树高度
        return 1 + max(getHeight(Node.getLeft()), getHeight(Node.getRight()))


def getBalanceFactor(Node):
    return getHeight(Node.getLeft()) - getHeight(Node.getRight())


def checkNode(Node):
    try:
        assert -1 <= getBalanceFactor(Node) <= 1
        if Node.getLeft() is not None:
            assert checkNode(Node.getLeft())
        if Node.getRight() is not None:
            assert checkNode(Node.getRight())
    except AssertionError:
        return False
    return True


def checkTree(dic):
    if dic.getRoot() is not None:
        try:
            assert checkNode(dic.getRoot())
        except AssertionError:
            return False
    return True


def treeShapeTest():
    dic1 = mydict()
    lst1 = [i for i in range(100000)]
    random.shuffle(lst1)
    lst1 = lst1[:1000]
    for item in lst1:  # 非负整数赋值
        dic1[item] = item
    for item in lst1:  # 负整数赋值
        dic1[-item] = -item
    lst2 = [random.uniform(1, 100000) for i in range(50)]
    for item in lst2:  # 浮点数赋值
        dic1[item] = item
    lst3 = [''.join([random.choice(char) for i in range(random.randint(0, 100))]) for j in range(50)]
    for item in lst3:  # 字符串赋值
        dic1[item] = item
    assert checkTree(dic1), "test point 6-1 break\nlst={}\ndic1={}".format(lst1 + lst2 + lst3, dic1)

    print("tree shape test pass.")


def test():
    setTest()
    getTest()
    delTest()
    basicTest()
    hashCrackTest()
    treeShapeTest()
    performanceTest()
    print("All tests pass.Congratulations!")
    print("Thanks for using. Contact me if you would like to support more examples.")


if __name__ == '__main__':
    test()
