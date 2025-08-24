# Gemma 3 270m Fine-Tuning Project

This project is designed to facilitate the fine-tuning of Google's Gemma 3 270m model using various techniques. It includes Jupyter notebooks that guide you through different fine-tuning methods, as well as utility scripts for data handling and configuration.

## Project Structure

- **src/**: Contains all source code, notebooks, and utilities.
  - **data/**: Directory for dataset-related files.
    - `README.md`: Documentation on the dataset used for fine-tuning.
  - **notebooks/**: Contains Jupyter notebooks for different fine-tuning techniques.
    - `finetune_gemma_3_270m.ipynb`: Main guide for fine-tuning the Gemma 3 270m model.
    - `lora_finetuning.ipynb`: Focuses on the LoRA (Low-Rank Adaptation) technique.
    - `qlora_finetuning.ipynb`: Covers the QLoRA (Quantized Low-Rank Adaptation) method.
    - `peft_finetuning.ipynb`: Discusses the PEFT (Parameter-Efficient Fine-Tuning) approach.
  - **utils/**: Contains utility functions for data handling.
    - `data_utils.py`: Functions for loading and preprocessing datasets.
  - `config.py`: Configuration settings for model parameters and training hyperparameters.

- `requirements.txt`: Lists the Python dependencies required for the project.

## Getting Started

1. **Clone the Repository**: Clone this repository to your local machine.
2. **Install Dependencies**: Navigate to the project directory and run:
   ```
   pip install -r requirements.txt
   ```
3. **Prepare Your Dataset**: Place your dataset in the `src/data/` directory and update the `src/data/README.md` with relevant information about the dataset.
4. **Run Notebooks**: Open the Jupyter notebooks in the `src/notebooks/` directory to start fine-tuning the Gemma 3 270m model using the techniques outlined.

## Fine-Tuning Techniques

- **LoRA**: A method that reduces the number of trainable parameters while maintaining model performance.
- **QLoRA**: A quantized version of LoRA that further optimizes memory usage and speed.
- **PEFT**: A parameter-efficient approach that fine-tunes only a subset of model parameters.

## Contributing

Feel free to contribute to this project by submitting issues or pull requests. Your feedback and improvements are welcome!

## License

This project is licensed under the MIT License. See the LICENSE file for details.