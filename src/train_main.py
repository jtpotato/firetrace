import os
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from torch.utils.data import DataLoader
import torch.nn as nn
import torch

from training.FiretraceData import FiretraceData
from training.FiretraceMLP import FiretraceMLP
from training.FiretraceImport import FiretraceImport
from training.training_loop import train_loop

X_train, X_test, y_train, y_test = FiretraceImport()

train_dataset = FiretraceData(X_train, y_train)

# print(X_train, y_train.values)

train_loader = DataLoader(dataset=train_dataset, batch_size=64, shuffle=True)

train_loop(X_test, y_test, train_loader, epoch_limit=1000000, retries=5)
