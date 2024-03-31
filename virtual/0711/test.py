

def plot_weight(weight):
    w_max = weight.max()
    w_min = weight.min()

    w_high_line = w_min + ((w_max-w_min)/3)*2
    w_low_line = w_min + ((w_max-w_min)/3)

    