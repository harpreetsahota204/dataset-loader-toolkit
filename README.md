# 📦 Dataset Loader Toolkit

The Dataset Loader Toolkit is a Python toolki that simplifies the process of loading and preprocessing datasets from the Hugging Face Hub. It provides a convenient way to configure and load multiple datasets using a YAML configuration file.

## 🌟 Features

- Load datasets from the Hugging Face Hub using a simple configuration file

- Preprocess datasets by removing or renaming columns

- Select a subset of the dataset for faster experimentation

- Modular and reusable code structure

- Robust error handling and logging

## 🚀 Installation

To use the Dataset Loader Toolkit, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/dataset-loader-toolkit.git
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## 💡 Usage

1. Create a YAML configuration file (e.g., `config.yaml`) specifying the datasets to load and their preprocessing options. Here's an example:

   ```yaml
   datasets:
     text_vqa_subset:
       dataset_name: "lmms-lab/textvqa"
       split: "train"
       subset_size: 1000
       remove_cols:
         - "image_id"
         - "question_id"
         - "question_tokens"
       # ...
   ```

2. Use the `DatasetLoader` class to load and preprocess the datasets:

   ```python
   from dataset_loader import DatasetLoader

   dataset_loader = DatasetLoader("config.yaml")
   dataset_loader.load_datasets()

   # Access the loaded datasets
   text_vqa_subset = dataset_loader.get_dataset("text_vqa_subset")
   ```

3. Use the loaded datasets in your application or scripts as needed.

## ⚙️ Configuration

The YAML configuration file allows you to specify various options for each dataset:

- `dataset_name`: The name of the dataset to load from the Hugging Face Hub.

- `split`: The desired split of the dataset (e.g., 'train', 'validation', 'test').

- `subset_size`: The size of the subset to select from the dataset (optional).

- `remove_cols`: A list of column names to remove from the dataset (optional).

- `rename_cols`: A dictionary specifying the columns to rename (optional).

- `dataset_kwargs`: Additional keyword arguments to pass to the `load_dataset` function (optional).

## 🤝 Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.