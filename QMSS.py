import pandas as pd


def reverse_this(var):
    """
    Note: in Pandas, you have to explicitly order the categorical variables yourself,
    either by passing `ordered=True` or specify an order

    :param var: Pandas dataframe column or series
        variable to reverse-code
    :return:
        reverse-coded variable
    """
    nvar = pd.to_numeric(var)
    var_max = nvar.max()
    var_min = nvar.min()
    var_sum = var_max + var_min
    var_reversed = var_sum - nvar

    if var.dtype.name == 'category' and var.cat.ordered:
        levs = var.cat.categories.tolist()
        c_reversed = pd.Categorical(var_reversed, categories=levs.reverse(), ordered=True)
        return c_reversed
    else:
        return var_reversed


def standardized_coef(fit, data):
    """
    :param fit:
        fitted model
    :param data: dataframe
        dataframe containing variables used to fit the model, with the dependent variable as the first column
    :return: Pandas series
        standardized coefficients
    """

    fit_params = fit.params[1:]
    sd = data.std()

    std_coef = fit_params*(sd[1:]/sd[0])

    return std_coef




