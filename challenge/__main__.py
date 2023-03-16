from pathlib import Path
from typing import Optional

import numpy as np
import numpy.typing as npt
import pandas as pd  # type: ignore
from typer import Typer, Option
from faker import Faker

GeneratorType = np.random._generator.Generator

app = Typer(add_completion=False)


@app.command()
def generate(
    records: int = Option(10000, help='number of records'),
    anomalies: int = Option(5, help='number of anomalies'),
    outfile: Path = Option(Path('./data.csv'), help='output csv'),
    seed: Optional[int] = Option(None, help='random seed')
) -> None:
    fake = Faker(['en_GB'])
    if seed:
        Faker.seed(seed)

    if seed:
        generator = np.random.default_rng(seed)
    else:
        generator = np.random.default_rng()

    fields = [
        'name',
        'birthdate'
        'sex',
        'blood_group',
        'address',
        'mail',
        'job',
        'company',
        'ssn',
    ]
    df = pd.DataFrame(fake.profile(fields) for i in range(records))
    df['height'] = heights(generator, number=records)
    insert_anomalies(generator, df, number=anomalies)

    df.to_csv(outfile, index=False)


def heights(generator: GeneratorType, number: int, mean: float = 168.6,
            sem: float = 0.13) -> npt.NDArray[np.float64]:

    standard_deviation = sem * np.sqrt(number)

    return np.around(generator.normal(
        loc=mean,
        scale=standard_deviation,
        size=number
    ), 2)


def insert_anomalies(generator: GeneratorType, df: pd.DataFrame,
                     number: int) -> None:
    for i in generator.choice(df.shape[0], number, replace=False):
        if generator.uniform() > 0.5:
            df.at[i, 'height'] = np.around(generator.uniform(1000, 2000), 2)
        else:
            df.at[i, 'height'] = np.around(generator.uniform(1, 10), 2)


@app.command()
def solve(
    infile: Path = Option(Path('./data.csv'), help='input data'),
    verbose: bool = Option(False, help='verbose information')
) -> None:
    df = pd.read_csv(infile)

    height = df['height']
    mean = height[(height <= 1000) & (height > 10)].mean()
    bad_mean = height.mean()

    if verbose:
        print('Height column summary')
        print(height.describe())
        print('\nLargest values')
        print(height.sort_values(ascending=False).head())
        print('\nSmallest values')
        print(height.sort_values().head())
        print('\n')

    print(
        f'The mean height is: {mean:.2f}\n'
        f'Without removing anomalies: {bad_mean:.2f}'
    )


if __name__ == '__main__':
    app()
