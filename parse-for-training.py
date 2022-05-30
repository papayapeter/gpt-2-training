import os
import json
import click


def error(s: str) -> None:
    print(s)
    raise SystemExit


@click.command()
@click.argument(
    'in_file', nargs=1, type=click.Path(exists=True, dir_okay=False)
    )
@click.argument('output', nargs=1, type=click.Path(dir_okay=False))
def parse(in_file: str, output: str) -> None:
    # read json and parse lines for textfile
    with open(in_file) as file:
        json_object = json.load(file)

    lines = [
        f'[{element["roleName"].upper()}:] {element["message"]}\n'
        for element in json_object
        ]

    # write textfile
    with open(output, 'w') as file:
        file.writelines(lines)


if __name__ == '__main__':
    parse()