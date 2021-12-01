load("@rules_python//python:defs.bzl", "py_binary", "py_library", "py_test")

py_library(
  name = "greeting_class",
  srcs = ["src/greeting_class.py"],
  visibility = ["//visibility:public"],
)

py_test(
  name = "test_greeting_class",
  srcs = ["test/test_greeting_class.py"],
  deps = [":greeting_class"]
)
