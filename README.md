Custom op compilation bug test case
===================================

See https://github.com/tensorflow/tensorflow/issues/23561.

To reproduce:

    pip install -e .
    ./bug

Expected error message:

    % ./bug 
    Traceback (most recent call last):
      File "./bug", line 8, in <module>
        tf.load_op_library(path)
      File "/usr/local/lib/python3.7/site-packages/tensorflow/python/framework/load_library.py", line 61, in load_op_library
        lib_handle = py_tf.TF_LoadLibrary(library_filename)
    tensorflow.python.framework.errors_impl.NotFoundError: dlopen(custom.cpython-37m-darwin.so, 6): Symbol not found: __ZN10tensorflow11GetNodeAttrERKNS_9AttrSliceENSt3__117basic_string_viewIcNS3_11char_traitsIcEEEEPNS3_12basic_stringIcS6_NS3_9allocatorIcEEEE
      Referenced from: custom.cpython-37m-darwin.so
      Expected in: flat namespace
     in custom.cpython-37m-darwin.so
