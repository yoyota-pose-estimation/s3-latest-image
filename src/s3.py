import datetime
import tensorflow as tf


def get_latest_images(path):
    pattern = f"s3://{path}"
    print(pattern)
    return {"images": tf.io.gfile.glob(pattern)}
