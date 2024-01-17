# -*- coding: utf-8 -*-
import click
import logging
import kaggle


@click.command()
@click.option(
    '-o', '--output-file-path', 'output_file_path',
    default='../../data/raw',
    help='Folder where file(s) will be downloaded.\n'
         'Default value: (<project_dir>/data/raw/)',
    type=click.Path(exists=True),
)
@click.option(
    '-d', '--dataset', 'dataset',
    default='sinamhd9/concrete-comprehensive-strength',
    help='Dataset URL suffix in format <owner>/<dataset-name>, '
         'or <owner>/<dataset-name>/<version-number> for a specific version.\n'
         'Default value: sinamhd9/concrete-comprehensive-strength',
)
def get_raw_data(output_file_path: str, dataset: str) -> None:
    """ Download raw data from Kaggle Concrete Compressive Strength dataset by
        Kaggle API and save it into (<project_dir>/data/raw/). In order to use
        the Kaggle’s public API an API token must be in the
        (~/.kaggle/kaggle.json).
    """

    log_fmt: str = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)
    logger: logging.Logger = logging.getLogger(__name__)

    kaggle.api.authenticate()
    logger.info('authenticated with Kaggle API')

    kaggle.api.dataset_download_files(
        dataset,
        path=output_file_path,
        unzip=True,
    )
    logger.info('downloaded raw data from Kaggle')


if __name__ == '__main__':
    get_raw_data()
