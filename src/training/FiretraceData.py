from torch.utils.data import Dataset

class FiretraceData(Dataset):
  def __init__(self, X, y):
    self.X = X
    self.y = y
    self.len = self.X.shape[0]

  def __getitem__(self, index):
    return self.X[index], self.y[index]
  
  def __len__(self):
    return self.len