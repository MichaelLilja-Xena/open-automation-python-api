import sys
print(sys.modules.get("xoa_driver.internals.hli_v1"))
if "xoa_driver.internals.hli_v1" in sys.modules:
    raise ImportError("\33[101mUsing xoa_driver and xoa_driver.v2 at the same time is not allowed.\33[0m")
