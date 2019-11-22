import datetime
import tensorflow as tf


def get_latest_images(path_prefix):
    now = datetime.datetime.utcnow()
    file_glob_pattern = now.strftime("%H:%M:%S")
    hour, minute = file_glob_pattern.split(":")[:2]
    pattern = "s3://{}/{}/{}/{}/*{}*".format(
        path_prefix, now.strftime("%Y-%m-%d"), hour, minute, file_glob_pattern
    )
    return {"images": tf.io.gfile.glob(pattern)}
