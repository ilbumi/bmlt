import torch

from bmlt.common import JsonLmdb
from bmlt.tabular.data import LMDBDataset


def test_lmdbdataset(tmp_path):
    tmp_folder = tmp_path / "sub"
    tmp_folder.mkdir()

    db_file = tmp_folder / "db.lmdb"
    with JsonLmdb.open(str(db_file), "c") as db:
        db["a"] = {
            "digit": 1,
            "list": [1, 2, 3],
        }
        db["b"] = {
            "digit": 1.0,
            "list": [1, 2, 3],
        }
        db["c"] = {
            "digit": 1,
            "list": [1, 2.0, "3"],
        }

    dataset = LMDBDataset(str(db_file))
    assert (dataset[0] == torch.tensor([1, 1, 2, 3])).all()
    assert (dataset[1] == torch.tensor([1, 1, 2, 3])).all()
    assert (dataset[2] == torch.tensor([1, 1, 2, 3])).all()

    assert dataset[0].dtype == torch.float32
