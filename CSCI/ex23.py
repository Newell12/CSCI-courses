def half1(x):
	return x-2
def half2(x):
	return x/2
def half3(x):
	return x/'2'

def test_half(func, x):
    try:
        if func(x)!=(x/2):
            return 'Incorrect'
        elif func(x)==(x/2):
            return 'Correct'
    except:
        return 'Error'
