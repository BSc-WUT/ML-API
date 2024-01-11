import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.utils.data as data

from src.models.generic import GenericModel
from src.models.operations import accuracy, sensitivity, precision, f1


class MLP(GenericModel):
    def __init__(
        self,
        device: torch.device,
        input_dim: int,
        output_dim: int,
    ):
        super().__init__(device)
        self.linear1 = nn.Linear(input_dim, 512)
        self.bn1 = nn.BatchNorm1d(512)
        self.linear2 = nn.Linear(512, 256)
        self.bn2 = nn.BatchNorm1d(256)
        self.linear3 = nn.Linear(256, 32)
        self.bn2 = nn.BatchNorm1d(32)
        self.linear4 = nn.Linear(32, output_dim)
        self.ReLU = nn.LeakyReLU()

    def forward(self, x):
        x = self.ReLU(self.bn1(self.linear1(x)))
        x = self.ReLU(self.bn2(self.linear2(x)))
        x = self.ReLU(self.bn3(self.linear3(x)))
        x = self.linear4(x)
        x = F.softmax(x, dim=1)
        return x


def evaluate_model(device, model: MLP, data_loader: data.DataLoader):
    model.eval()
    true_predictions, predicitons_amount, false_negative, false_positive = (
        0.0,
        0.0,
        0.0,
        0.0,
    )

    total_steps = len(data_loader)

    with torch.no_grad():
        for step, (inputs, labels) in enumerate(data_loader):
            # Progress Bar
            progress = (step + 1) / total_steps
            progress = (step + 1) / total_steps
            progress_bar = (
                "[" + "=" * int(50 * progress) + " " * (50 - int(50 * progress)) + "]"
            )
            print(
                f"\r{progress_bar} {step + 1}/{total_steps} batches processed", end=""
            )
            inputs = inputs.to(device)
            labels = labels.to(device)

            preds = model(inputs)
            pred_labels = preds.to(device)

            true_predictions += (pred_labels == labels).sum().item()
            false_positive += (
                ((pred_labels != labels) & (pred_labels == 0) & (labels != 0))
                .sum()
                .item()
            )
            false_negative += (
                ((pred_labels != labels) & (pred_labels != 0) & (labels == 0))
                .sum()
                .item()
            )
            predicitons_amount += len(pred_labels)

        acc = accuracy(true_predictions, predicitons_amount)
        prec = precision(true_predictions, false_positive)
        sens = sensitivity(true_predictions, false_negative)
        f1_value = f1(prec, sens)

    print(f"Accuracy: {acc:4.2f}%")
    print(f"Precision: {prec:4.2f}")
    print(f"Sensitivity: {sens:4.2f}")
    print(f"F1: {f1_value:4.2f}")
