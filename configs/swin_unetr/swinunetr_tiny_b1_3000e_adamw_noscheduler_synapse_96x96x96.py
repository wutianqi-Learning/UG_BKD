from mmengine.config import read_base
from monai.losses import DiceCELoss
from monai.networks.nets import SwinUNETR
from seg.models.segmentors.monai_model import MonaiSeg

with read_base():
    from .._base_.datasets.synapse import *  # noqa
    from .._base_.schedules.schedule_1000e_adamw_noscheduler import *  # noqa
    from .._base_.monai_runtime import *  # noqa

train_cfg = dict(type=EpochBasedTrainLoop, max_epochs=3000, val_begin=200, val_interval=100)

dataloader_cfg.update(
    dict(num_samples=1)
)

# model settings
model = dict(
    type=MonaiSeg,
    num_classes=14,
    roi_shapes=roi,
    backbone=dict(
        type=SwinUNETR,
        img_size=roi,
        feature_size=12,
        in_channels=1,
        out_channels=14,
        spatial_dims=3),
    loss_functions=dict(
        type=DiceCELoss, to_onehot_y=True, softmax=True),
    infer_cfg=dict(
        inf_size=roi,
        sw_batch_size=1,    # number of sliding window batch size
        infer_overlap=0.5   # sliding window inference overlap
    ))
