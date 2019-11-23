import datetime
import tensorflow as tf


def get_latest_images(path_prefix, time):
    if not time:
        time = datetime.datetime.utcnow() - datetime.timedelta(seconds=2)
        time = str(time.isoformat()).split(".")[0]
    ymd, hms = time.split("T")
    hour, minute = hms.split(":")[:2]
    pattern = "s3://{}/{}/{}/{}/*{}*".format(
        path_prefix, ymd, hour, minute, hms
    )
    return {"images": tf.io.gfile.glob(pattern)}
