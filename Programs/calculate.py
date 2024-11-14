import circle
import square

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
        raise ValueError(f"Unknown figure: {fig}. \
        Available figures are {figs}.")
    if func not in funcs:
        raise ValueError(f"Unknown command: {func}. \
        Available functions are {funcs}.")

    if len(size) != sizes.get(f"{fig}-{func}", 1):
        raise ValueError(f"Expected {sizes.get(f'{fig}-{func}', 1)}\ "
                         f"values for {fig} {func}, but got {len(size)}.")

    try:
        if fig == 'circle':
            module = circle
        elif fig == 'square':
            module = square
        else:
            raise ValueError(f"Unsupported figure: {fig}")

        function = getattr(module, func)
        result = function(*size)
        return result

    except Exception as e:
        raise ValueError(f"Error calculating {func} of \ "
                         f"{fig} with size {size}: {e}")


def get_figure_result():
    fig = ''
    func = ''
    size = list()

    # Вводим фигуру
    while fig not in figs:
        fig = input(f"Enter figure name, available are {figs}:\n")

    while func not in funcs:
        func = input(f"Enter function name, available are {funcs}:\n")

    while len(size) != sizes.get(f"{func}-{fig}", 1):
        try:
            size = list(map(int, input(
                f"Input figure sizes separated by space (expected \ "
                f"{sizes.get(f'{func}-{fig}', 1)} values):\n").split()))
            if len(size) != sizes.get(f"{func}-{fig}", 1):
                print(f"Expected {sizes.get(f'{func}-{fig}', 1)} \ "
                      f"values, you entered {len(size)}. Please try again.")
        except ValueError:
            print("Invalid input! Please enter numbers only.")

    return calc(fig, func, size)


if __name__ == "__main__":
    result = get_figure_result()
    print(f"The result is: {result}")
