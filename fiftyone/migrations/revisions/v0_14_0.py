"""
FiftyOne v0.14.0 revision.

| Copyright 2017-2021, Voxel51, Inc.
| `voxel51.com <https://voxel51.com/>`_
|
"""


def up(db, dataset_name):
    match_d = {"name": dataset_name}
    dataset_dict = db.datasets.find_one(match_d)

    if "frame_collection_name" not in dataset_dict:
        name = "frames." + dataset_dict["sample_collection_name"]
        dataset_dict["frame_collection_name"] = name

    db.datasets.replace_one(match_d, dataset_dict)


def down(db, dataset_name):
    match_d = {"name": dataset_name}
    dataset_dict = db.datasets.find_one(match_d)

    dataset_dict.pop("frame_collection_name", None)

    db.datasets.replace_one(match_d, dataset_dict)
