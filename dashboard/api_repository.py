from fastapi import APIRouter
import os

from storage.models import get_latest_scan

router = APIRouter()


def get_items(relative_path=""):

    latest = get_latest_scan()

    if not latest:
        return []

    root = latest["repository"]

    folder = os.path.join(root, relative_path)

    if not os.path.isdir(folder):
        return []

    items = []

    for name in sorted(os.listdir(folder)):

        full = os.path.join(folder, name)

        items.append(
            {
                "name": name,
                "path": os.path.join(relative_path, name).replace("\\", "/"),
                "folder": os.path.isdir(full),
            }
        )

    return items


@router.get("/repository")
def repository(path: str = ""):

    return get_items(path)