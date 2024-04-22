import yaml
import logging
from datasets import load_dataset

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class DatasetLoader:
    def __init__(self, config_file):
        self.config_file = config_file
        self.datasets = {}

    def load_config(self):
        try:
            with open(self.config_file, "r") as f:
                config = yaml.safe_load(f)
            return config
        except FileNotFoundError:
            logger.error(f"Configuration file not found: {self.config_file}")
            raise
        except yaml.YAMLError as exc:
            logger.error(f"Error parsing YAML file: {exc}")
            raise

    def load_and_preprocess_dataset(self, dataset_name, split, subset_size=None, remove_cols=None, rename_cols=None, **dataset_kwargs):
        try:
            dataset = load_dataset(dataset_name, split=split, **dataset_kwargs)
        except Exception as e:
            logger.error(f"Error loading dataset '{dataset_name}': {e}")
            raise

        if subset_size:
            dataset = dataset.shuffle(seed=51).select(range(subset_size))

        if remove_cols:
            dataset = dataset.remove_columns(remove_cols)

        if rename_cols:
            dataset = dataset.rename_columns(rename_cols)

        dataset = dataset.add_column('source', [dataset_name] * len(dataset))

        return dataset

    def load_datasets(self):
        config = self.load_config()

        for dataset_id, dataset_config in config["datasets"].items():
            try:
                dataset = self.load_and_preprocess_dataset(
                    dataset_config["dataset_name"],
                    split=dataset_config["split"],
                    subset_size=dataset_config.get("subset_size"),
                    remove_cols=dataset_config.get("remove_cols"),
                    rename_cols=dataset_config.get("rename_cols"),
                    **dataset_config.get("dataset_kwargs", {})
                )
                self.datasets[dataset_id] = dataset
                logger.info(f"Loaded and preprocessed dataset: {dataset_id}")
            except Exception as e:
                logger.error(f"Error loading dataset '{dataset_id}': {e}")

    def get_dataset(self, dataset_id):
        return self.datasets.get(dataset_id)

