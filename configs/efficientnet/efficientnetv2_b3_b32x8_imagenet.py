_base_ = [
    '../_base_/models/efficientnet/tf_efficientnetv2_b3.py', '../_base_/datasets/imagenet_bs32_240.py',
    '../_base_/schedules/imagenet_bs256.py', '../_base_/default_runtime.py'
]
