import chimerapy as cp
from chimerapy_orchestrator import source_node

from mmlapipe.generic_nodes.video_nodes import Video
from mmlapipe.pose.data import YOLOFrame


@source_node(name="YOLOVideo")
class YOLOVideo(Video):
    """A video node that returns a Frame object with identifiable metadata."""

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.include_meta = True

    def step(self) -> cp.DataChunk:
        data_chunk = super().step()
        ret_chunk = cp.DataChunk()
        frame_arr = data_chunk.get(self.frame_key)["value"]
        src_id = data_chunk.get("metadata")["value"]["source_name"]
        frame_count = data_chunk.get("metadata")["value"]["frame_count"]

        ret_chunk.add(
            self.frame_key,
            [YOLOFrame(frame_arr, src_id=src_id, frame_count=frame_count)],
        )

        return ret_chunk