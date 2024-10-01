from mmengine.config import read_base
from monai.losses import DiceCELoss
from monai.networks.nets import UNETR
from seg.models.segmentors.monai_model import MonaiSeg

with read_base():
    from .._base_.datasets.word import *  # noqa
    from .._base_.schedules.schedule_1000e_adamw import *  # noqa
    from .._base_.monai_runtime import *  # noqa

dataloader_cfg.update(
    dict(num_samples=2)
)

load_from = 'ckpts/UNETR_model_best_acc_mmengine.pth'

# model settings
model = dict(
    type=MonaiSeg,
    num_classes=17,
    roi_shapes=roi,
    backbone=dict(
        type=UNETR,
        img_size=roi,
        # feature_size=48,
        pos_embed='perceptron',
        in_channels=1,
        out_channels=17,
        spatial_dims=3),
    loss_functions=dict(
        type=DiceCELoss, to_onehot_y=True, softmax=True),
    infer_cfg=dict(
        inf_size=roi,
        sw_batch_size=2,    # number of sliding window batch size
        infer_overlap=0.5   # sliding window inference overlap
    ))