import pickle
import test_sub_custom as t
'''
This module pickles your custom test module. It introspects to discover all test classes
(with base class = TestBaseClass) and adds them to the pickle.
The name of the pickle file is the same as the name of the module.
TODO: Substitute the name of your module in the line above (import xxx as t).
TODO: run: python custom_test_pickler.py
TODO: include the generated .p file in your operational folder.
'''
test_classes = []
class_names_in_module = [elem for elem in dir(t) if "_" not in elem]
index = class_names_in_module.index("TestBaseClass")
del class_names_in_module[index]

classes_in_module = [getattr(t, elem) for elem in class_names_in_module]

pickle.dump(classes_in_module, open( t.__name__ + ".p", "wb" ))
