_base_ = [
    '../_base_/models/efficientnet/tf_efficientnetv2_s.py', '../_base_/datasets/imagenet_bs32_300.py',
    '../_base_/schedules/imagenet_bs256.py', '../_base_/default_runtime.py'
]
