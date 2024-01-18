# -*- coding: utf-8 -*-
import logging

import click
import kaggle

raw_data_logger = logging.getLogger(__name__)
raw_data_logger.setLevel(logging.INFO)

raw_data_handler: logging.FileHandler = logging.FileHandler(
    f'./.logs/{__name__}.log', mode='w'
)
raw_data_formatter: logging.Formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

raw_data_handler.setFormatter(raw_data_formatter)
raw_data_logger.addHandler(raw_data_handler)


@click.command()
@click.option(
    '-o', '--output-file-path', 'output_file_path',
    default='../../data/raw',
    help='Path to the folder where file(s) will be downloaded. '
         'The default value is <project_dir>/data/raw/ .',
    type=click.Path(exists=True),
)
@click.option(
    '-d', '--dataset', 'dataset',
    default='sinamhd9/concrete-comprehensive-strength',
    help='Dataset URL suffix in format <owner>/<dataset-name>, '
         'or <owner>/<dataset-name>/<version-number> for a specific version. '
         'The default value is sinamhd9/concrete-comprehensive-strength .',
)
def get_raw_data(output_file_path: str, dataset: str) -> None:
    """ Download raw dataset from Kaggle.

        By default download Concrete Compressive Strength dataset with
        Kaggle API and save it into <project_dir>/data/raw/ . In order to use
        the Kaggle`s public API an API token must be in the
        ~/.kaggle/kaggle.json .\f

        Parameters
        ----------
        output_file_path : str, optional
            Path to the folder where file(s) will be downloaded.
            The default value: <project_dir>/data/raw/ .
        dataset : str, optional
            Dataset URL suffix in format <owner>/<dataset-name>, or
            <owner>/<dataset-name>/<version-number> for a specific version.
            The default value is sinamhd9/concrete-comprehensive-strength .'
    """

    raw_data_logger.info('get raw data from Kaggle API')

    kaggle.api.dataset_download_files(
        dataset,
        path=output_file_path,
        unzip=True,
    )

    raw_data_logger.info('downloaded raw data from Kaggle')


if __name__ == '__main__':
    get_raw_data()
