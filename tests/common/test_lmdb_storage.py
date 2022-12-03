from bmlt.common import JsonLmdb


def test_jsonlmdb(tmp_path):
    tmp_folder = tmp_path / "sub"
    tmp_folder.mkdir()

    db_file = tmp_folder / "db.lmdb"
    with JsonLmdb.open(str(db_file), "c") as db:
        db["a"] = {
            "digit": 1,
            "list": [1, 2, 3],
            "alpha_list": ["1", "a", "b"],
            "alpha_digit": "2",
        }
        assert db["a"]["digit"] == 1
        assert db["a"]["list"] == [1, 2, 3]
        assert db["a"]["alpha_list"] == ["1", "a", "b"]
        assert db["a"]["alpha_digit"] == "2"

        assert len(db) == 1
        del db["a"]
        assert len(db) == 0
