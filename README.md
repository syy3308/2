
## Data Structure
Please make sure the folder structure of prepared dataset is organized as followed:

```
<dataset_root>
├── images_test
│   ├── 1066405,100a000985ef070.jpg
│   ├── 1066405,138f000e0722fb6.jpg
│   ├── 1066405,145000347015bf.jpg
│   ├── 1066405,19c000252c07c1.jpg
│   ├── 1066405,1b8000ef60354f.jpg
│   └── ...
├── Images
│   ├── 273271,1017c000ac1360b7.jpg
│   ├── 273271,10355000e3a458a6.jpg
│   ├── 273271,1039400091556057.jpg
│   ├── 273271,104ec00067d5b782.jpg
│   ├── 273271,1050b000e40d8e93.jpg
│   └── ...
├── annotation_train.odgt
└── annotation_val.odgt
```

The folder structure of dsdl annotation for Object Detection is organized as followed:

```
<dsdl_root>
├── set-train
│   ├── train.yaml
│   └── train_samples.json
├── defs
│   ├── class-domain.yaml
│   └── crowdhuman-detection-def.yaml
├── set-val
│   ├── val.yaml
│   └── val_samples.json
├── set-test
│   ├── test.yaml
│   └── test_samples.json
├── README.md
└── config.py
```

## config.py
You can load your dataset from local or oss.
From local:

```
local = dict(
    type="LocalFileReader",
    working_dir="the root path of the prepared dataset",
)
```

Please change the 'working_dir' to the path of your prepared dataset where media data can be found,
for example: "<root>/dataset_name/prepared".

From oss:

```
ali_oss = dict(
    type="AliOSSFileReader",
    access_key_secret="your secret key of aliyun oss",
    endpoint="your endpoint of aliyun oss",
    access_key_id="your access key of aliyun oss",
    bucket_name="your bucket name of aliyun oss",
    working_dir="the prefix of the prepared dataset within the bucket")
```

Please change the 'access_key_secret', 'endpoint', 'access_key_id', 'bucket_name' and 'working_dir',
e.g. if the full path of your prepared dataset is "oss://bucket_name/dataset_name/prepared", then the working_dir should be "dataset_name/prepared".

## Related source:
1. Get more information about DSDL: [dsdl-docs](https://opendatalab.github.io/dsdl-docs/)
2. DSDL-SDK official repo: [dsdl-sdk](https://github.com/opendatalab/dsdl-sdk/)
3. Get more dataset: [OpenDataLab](https://opendatalab.com/)
