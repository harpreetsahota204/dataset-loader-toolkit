import yaml
import logging
from datasets import load_dataset

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def load_config(config_file):
    """
    Load the YAML configuration file.

    Args:
        config_file (str): Path to the YAML configuration file.

    Returns:
        dict: Parsed configuration dictionary.

    Raises:
        FileNotFoundError: If the configuration file is not found.
        yaml.YAMLError: If there is an error parsing the YAML file.
    """
    try:
        with open(config_file, "r") as f:
            config = yaml.safe_load(f)
        return config
    except FileNotFoundError:
        logger.error(f"Configuration file not found: {config_file}")
        raise
    except yaml.YAMLError as exc:
        logger.error(f"Error parsing YAML file: {exc}")
        raise

def load_and_preprocess_dataset(dataset_config):
    """
    Load and preprocess a dataset based on the provided configuration.

    Args:
        dataset_config (dict): Dataset configuration dictionary.

    Returns:
        Dataset: Preprocessed dataset.

    Raises:
        Exception: If there is an error loading the dataset.
    """
    try:
        # Load the dataset using the provided configuration
        dataset = load_dataset(
            dataset_config["dataset_name"],
            split=dataset_config["split"],
            **dataset_config.get("dataset_kwargs", {})
        )
    except Exception as e:
        logger.error(f"Error loading dataset '{dataset_config['dataset_name']}': {e}")
        raise

    # Apply subset selection if specified in the configuration
    if "subset_size" in dataset_config:
        dataset = dataset.shuffle(seed=51).select(range(dataset_config["subset_size"]))

    # Remove columns if specified in the configuration
    if "remove_cols" in dataset_config:
        dataset = dataset.remove_columns(dataset_config["remove_cols"])

    # Rename columns if specified in the configuration
    if "rename_cols" in dataset_config:
        dataset = dataset.rename_columns(dataset_config["rename_cols"])

    # Add a 'source' column with the dataset name
    dataset = dataset.add_column('source', [dataset_config["dataset_name"]] * len(dataset))

    return dataset

def load_dataset_from_config(config_file, dataset_id):
    """
    Load a specific dataset from the configuration file.

    Args:
        config_file (str): Path to the YAML configuration file.
        dataset_id (str): ID of the dataset to load.

    Returns:
        Dataset: Preprocessed dataset.
        None: If the specified dataset ID is not found in the configuration.
    """
    # Load the entire configuration from the file
    config = load_config(config_file)
    
    # Check if the specified dataset ID exists in the configuration
    if dataset_id in config["datasets"]:
        # Retrieve the configuration for the specified dataset
        dataset_config = config["datasets"][dataset_id]
        
        # Load and preprocess the dataset using the retrieved configuration
        dataset = load_and_preprocess_dataset(dataset_config)
        return dataset
    else:
        logger.warning(f"Dataset '{dataset_id}' not found in the configuration file.")
        return None