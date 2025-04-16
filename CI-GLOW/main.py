# main.py

import torch
import torch.optim as optim
from training.trainer import Trainer
from configs.config import Config
from models.model import model_builder
from data.data_loader import data_loader
from training.optimizer import build_optimizer


def main():
    # Load configuration
    config = Config()

    # Initialize the model
    model = model_builder(config=config.model)

    # Prepare the dataset and dataloaders
    data = data_loader(config=config.data)

    # Optimizer and learning rate scheduler
    optimizer = build_optimizer(model, config.training)

    # Scheduler (optional, for learning rate decay)
    scheduler = optim.lr_scheduler.StepLR(optimizer, step_size=10, gamma=0.1)

    # Initialize the trainer with the model, data, optimizer, and config
    trainer = Trainer(
        model=model,
        data=data,
        scheduler=scheduler,
        config=config,
        # optimizer, loss func, logdir build from config
    )

    # Start the training
    trainer.train(epochs=config.num_epochs)


if __name__ == "__main__":
    main()
