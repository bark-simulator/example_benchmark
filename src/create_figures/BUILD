
filegroup(
  name = "notebooks_folder",
  srcs = glob(["*.ipynb"], exclude=["run.py", "run", "__init__.py"])
)

# add bark deps here
py_test(
  name = "run_notebooks",
  srcs = ["run_notebooks.py"],
  data = [":notebooks_folder",
          "@bark_project//bark/python_wrapper:core.so",
          "//results/benchmark:benchmark_results",
          ],
  deps = ["@bark_project//bark/benchmark:benchmark_runner",
          ],
)