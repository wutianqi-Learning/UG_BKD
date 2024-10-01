from mmengine.config import read_base
with read_base():
    from ..unet.unetmod_base_d8_1000e_sgd_synapse_96x96x96 import * # noqa

dataloader_cfg.update(
    dict(num_samples=1)
)
# model settings
model.update(
    dict(
        backbone=dict(
            num_res_units=0)))