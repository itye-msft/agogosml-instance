import os
import pickle
import test_sub_custom_one as t1
import test_sub_custom_two as t2
import test_sub_builtIn as t3
import inspect

'''
This module pickles the custom test modules. It introspects to discover all test classes
(with base class = TestBaseClass) and adds them to the pickle.
The name of the pickle file is the same as the name of the module.
If you make a new custom test module, add it to the list above and adjust below.
'''
def remove_test_base_class(class_names):
    index = class_names.index("TestBaseClass")
    del class_names[index]
    return class_names

def remove_non_class_elements_and_pickle(classes_in_module, import_name):
    for index in reversed(range(len(classes_in_module))):
        if not inspect.isclass(classes_in_module[index]):
            del classes_in_module[index]
    pickle.dump(classes_in_module, open( import_name + ".p", "wb" ))

print('current directory is: ' + os.getcwd())
print('tests directory exists: %s' % os.path.exists('tests'))
if os.path.exists('tests'):
    os.chdir('tests/test-generator/generator-python')
print('current directory is: ' + os.getcwd())

# t1
elements_in_t1 = [elem for elem in dir(t1) if elem[0] != '_']
class_names_in_t1 = remove_test_base_class(elements_in_t1)
classes_in_t1 = [getattr(t1, elem) for elem in class_names_in_t1]
remove_non_class_elements_and_pickle(classes_in_t1, t1.__name__)

# t2
elements_in_t2 = [elem for elem in dir(t2) if elem[0] != '_']
class_names_in_t2 = remove_test_base_class(elements_in_t2)
classes_in_t2 = [getattr(t2, elem) for elem in class_names_in_t2]
remove_non_class_elements_and_pickle(classes_in_t2, t2.__name__)

# t3
elements_in_t3 = [elem for elem in dir(t3) if elem[0] != '_']
class_names_in_t3 = remove_test_base_class(elements_in_t3)
classes_in_t3 = [getattr(t3, elem) for elem in class_names_in_t3]
remove_non_class_elements_and_pickle(classes_in_t3, t3.__name__)

