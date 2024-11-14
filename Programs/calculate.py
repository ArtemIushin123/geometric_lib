figs = ['circle', 'square']
funcs = ['perimeter', 'area']
sizes = {
    'circle-area': 1,
    'circle-perimeter': 1,
    'square-area': 1,
    'square-perimeter': 1,
}


def calc(fig, func, size):
    if fig not in figs:
        raise ValueError(f"Unknown figure: {fig}. Available figures are {figs}.")

    if func not in funcs:
        raise ValueError(f"Unknown command: {func}. Available functions are {funcs}.")

    try:
        module = globals()[fig]
        function = getattr(module, func)
        result = function(*size)
        return result
    except Exception as e:
        raise ValueError(f"Error calculating {func} of {fig} with size {size}: {e}")


def get_figure_result():
    func = ''
    fig = ''
    size = list()

    while fig not in figs:
        fig = input(f"Enter figure name, available are {figs}:\n")

    while func not in funcs:
        func = input(f"Enter function name, available are {funcs}:\n")

    while len(size) != sizes.get(f"{func}-{fig}", 1):
        try:
            size = list(map(int, input(
                f"Input figure sizes separated by space (expected {sizes.get(f'{func}-{fig}', 1)} values):\n"
            ).split()))
            if len(size) != sizes.get(f"{func}-{fig}", 1):
                print(f"Expected {sizes.get(f'{func}-{fig}', 1)} values, you entered {len(size)}. Please try again.")
        except ValueError:
            print("Invalid input! Please enter numbers only.")

    result = calc(fig, func, size)
    return result


if __name__ == "__main__":
    result = get_figure_result()
    print(f"Result: {result}")
