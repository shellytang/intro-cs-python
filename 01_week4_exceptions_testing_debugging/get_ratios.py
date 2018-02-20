def get_ratios(L1, L2):
    '''
    Assumes: L1 and L2 are lists of equal lengths of numbers
    Returns: a list container L1[i]/L2[i]
    '''
    ratios = []
    for index in range(len(L1)):
        try:
            ratios.append(L1[index]/float(L2[index]))
        except ZeroDivisionError:
            ratios.append(float('NaN'))
        except:
            raise ValueError('get_ratios called with bad args')
    return ratios

L1 = [2,3,4,5]
L2 = [6,7,8,9]
L3 = [8,9]
L4 = [6,7,8,0]
print(get_ratios(L1, L4))