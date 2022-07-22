paramwise_cfg = dict(
    norm_decay_mult=0.0,
    bias_decay_mult=0.0,
)

# for batch in each gpu is 64, 8 gpu
# lr = 5e-4 * 64 * 8 / 512 = 0.0005
optimizer = dict(
    type='AdamW',
    lr=5e-4 * 64 * 8 / 512,
    weight_decay=0.05,
    eps=1e-8,
    betas=(0.9, 0.999),
    paramwise_cfg=paramwise_cfg)
optimizer_config = dict(grad_clip=dict(max_norm=5.0))

# learning policy
lr_config = dict(
    policy='CosineAnnealing',
    by_epoch=False,
    min_lr_ratio=1e-2,
    warmup='linear',
    warmup_ratio=1e-3,
    warmup_iters=20 * 1252,
    warmup_by_epoch=False)

runner = dict(type='EpochBasedRunner', max_epochs=300)
