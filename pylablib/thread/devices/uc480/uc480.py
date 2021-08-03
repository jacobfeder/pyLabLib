from ..generic import camera
from ....devices import uc480

class UC480CameraThread(camera.GenericCameraThread):
    """
    Generic uc480 camera device thread.

    See :class:`GenericCameraThread`.
    """
    parameter_variables=camera.GenericCameraThread.parameter_variables|{"exposure","frame_period","detector_size","pixel_rate","buffer_size","acq_status","roi_limits","roi"}
    _frameinfo_include_fields={ "frame_index","framestamp","timestamp_dev","io_status",
                                "timestamp_year","timestamp_month","timestamp_day","timestamp_hour","timestamp_minute","timestamp_second","timestamp_millisecond"}
    def connect_device(self):
        with self.using_devclass("uc480.UC480Camera",host=self.remote) as cls:
            if self.sn is not None:
                dev_id=uc480.find_by_serial(serial_number=self.sn)
                self.device=cls(dev_id=dev_id)
            else:
                self.device=cls(cam_id=self.id)
    def setup_task(self, idx, dev_idx=None, sn=None, remote=None, misc=None):
        self.id=idx
        self.dev_id=dev_idx
        self.sn=sn
        super().setup_task(remote=remote,misc=misc)