
import pandas as pd
print("hello from python on ubuntu on windows!")

def func(a):
    """
    Test debugging
    """
    if a == 3:
        return None
    else:
        print(a)

    return None
b_df = pd.DataFrame(data={'col1': [1, 2], 'col2': [3, 4]})
b = 2
func("Second print")
func(b)
func(b_df)
func(b=3)
