checkpoint_config = dict(interval=4)
# yapf:disable
log_config = dict(
    interval=500,
    hooks=[
        dict(type="TextLoggerHook", interval=500),
        dict(
            type="MMDetWandbHook",
            init_kwargs={
                "project": "trash_object_detection",
                "entity": "cv_09_detection",
                "name": "UniverseNet_r101",
            },
            interval=1000,
            log_checkpoint=False,
            log_checkpoint_metadata=True,
            num_eval_images=0,
        )
        # dict(type='TensorboardLoggerHook')
    ],
)
# yapf:enable
custom_hooks = [dict(type="NumClassCheckHook")]

dist_params = dict(backend="nccl")
log_level = "INFO"
load_from = None
resume_from = None
workflow = [("train", 1)]

# disable opencv multithreading to avoid system being overloaded
opencv_num_threads = 0
# set multi-process start method as `fork` to speed up the training
mp_start_method = "fork"

# Default setting for scaling LR automatically
#   - `enable` means enable scaling LR automatically
#       or not by default.
#   - `base_batch_size` = (8 GPUs) x (2 samples per GPU).
auto_scale_lr = dict(enable=False, base_batch_size=16)
