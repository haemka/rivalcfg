import os


DEBUG_DRY = "DEBUG_DRY" in os.environ

DEBUG_PROFILE_VENDOR_ID = None
DEBUG_PROFILE_PRODUCT_ID = None
if "DEBUG_PROFILE" in os.environ:
    DEBUG_PROFILE_VENDOR_ID = os.environ["DEBUG_PROFILE"].split(":")[0]
    DEBUG_PROFILE_PRODUCT_ID = os.environ["DEBUG_PROFILE"].split(":")[1]

DEBUG_DEVICE_VENDOR_ID = None
DEBUG_DEVICE_PRODUCT_ID = None
if "DEBUG_DEVICE" in os.environ:
    DEBUG_DEVICE_VENDOR_ID = os.environ["DEBUG_DEVICE"].split(":")[0]
    DEBUG_DEVICE_PRODUCT_ID = os.environ["DEBUG_DEVICE"].split(":")[1]

DEBUG = DEBUG_DRY or DEBUG_PROFILE_VENDOR_ID or DEBUG_DEVICE_VENDOR_ID