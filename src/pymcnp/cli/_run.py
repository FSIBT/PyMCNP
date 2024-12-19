import importlib
import subprocess


def main():
    prehook = importlib.import_module('prehook')
    posthook = importlib.import_module('posthook')

    path = __file__.split('/')
    name = path[-1].split('.')[0]

    prehook.main(path[:-1], name)
    subprocess.run(name, shell=True)
    posthook.main(path[:-1], name)


if __name__ == '__main__':
    main()
