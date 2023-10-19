from pathlib import Path

import torch
import torch.nn as nn

from .const import CHAR_TO_INDEX, INDEX_TO_CHAR, VOCAB_SIZE
from .ikea import RNN

MODEL_PATH = Path(__file__).resolve().parent / "model_scripted.pt"


def load_model() -> RNN:
    if not MODEL_PATH.exists():
        raise FileNotFoundError(
            f"Model not found at {MODEL_PATH}. "
            "Please run `python src/model/ikea.py` to generate it."
        )

    model = torch.jit.load("./src/model/model_scripted.pt")
    return model


def is_query_valid(query: str) -> bool:
    return all(ch in CHAR_TO_INDEX for ch in query)


def _predict(model: RNN, characters: list[str]) -> tuple[str, torch.Tensor]:
    start = torch.zeros(size=(1, len(characters), VOCAB_SIZE))

    for idx, ch in enumerate(characters):
        start[0][idx][CHAR_TO_INDEX[ch]] = 1

    out, hidden = model(start)

    prob = nn.functional.softmax(out[-1], dim=0).data

    char_ind = int(torch.max(prob, dim=0)[1].item())

    return INDEX_TO_CHAR[char_ind], hidden


def sample(model: RNN, start="h") -> str:
    model.eval()
    start = start.lower()
    chars = [ch for ch in start]
    size = 20 - len(chars)

    for _ in range(size):
        char, _ = _predict(model, chars)
        chars.append(char)

    return "".join(chars).strip()
