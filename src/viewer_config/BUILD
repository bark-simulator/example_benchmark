py_library(
  name = "viewer_config",
  srcs = ["viewer_config.py"],
  data = ["@bark_project//bark/python_wrapper:core.so"],
  imports = ['../python/'],
  deps = ["@bark_project//bark/runtime"],
   visibility = ["//visibility:public"],
)

py_test(
  name = "viewer_config_test",
  srcs = ["viewer_config_test.py"],
  data = ["@bark_project//bark/python_wrapper:core.so",
          "//src/viewer_config/params:viewer_params"],
  imports = ['../python/'],
  deps = [":viewer_config"]
)
