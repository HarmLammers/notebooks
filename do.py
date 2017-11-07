import begin


@begin.subcommand
def test():
    print('BINGO!')


@begin.start
def run():
    pass
