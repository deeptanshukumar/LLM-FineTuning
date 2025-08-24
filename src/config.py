import os

class Config:
    def __init__(self):
        # Model configuration
        self.model_name = "gemma-3-270m"
        self.model_path = os.path.join("models", self.model_name)
        
        # Training configuration
        self.epochs = 3
        self.batch_size = 16
        self.learning_rate = 5e-5
        self.warmup_steps = 500
        self.logging_steps = 100
        self.save_steps = 500
        
        # Data configuration
        self.dataset_path = os.path.join("data", "dataset.csv")
        self.output_dir = os.path.join("output", self.model_name)
        
        # GPU configuration
        self.use_gpu = True  # Set to False if you want to run on CPU
        self.gpu_device = "cuda:0" if self.use_gpu else "cpu"

    def display_config(self):
        print("Model Name:", self.model_name)
        print("Model Path:", self.model_path)
        print("Epochs:", self.epochs)
        print("Batch Size:", self.batch_size)
        print("Learning Rate:", self.learning_rate)
        print("Warmup Steps:", self.warmup_steps)
        print("Logging Steps:", self.logging_steps)
        print("Save Steps:", self.save_steps)
        print("Dataset Path:", self.dataset_path)
        print("Output Directory:", self.output_dir)
        print("Using GPU:", self.use_gpu)
        print("GPU Device:", self.gpu_device)