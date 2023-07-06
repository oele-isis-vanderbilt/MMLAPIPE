from dataclasses import dataclass
from typing import Optional

import numpy as np
from ultralytics.yolo.engine.results import Results


@dataclass
class YOLOFrame:
    """A frame from a video source."""

    arr: np.ndarray
    frame_count: int
    src_id: str
    result: Optional[Results] = None

    def __repr__(self) -> str:
        return f"<Frame from {self.src_id} {self.frame_count}>"