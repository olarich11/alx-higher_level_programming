#include <Python.h>

/**
 * print_python_list_info - Prints basic info about Python lists.
 * @p: A PyObject list.
 */
void print_python_list_info(PyObject *p)
{
    int size = PyList_Size(p);
    int i;
    PyListObject *list = (PyListObject *)p;

    printf("[*] Size of the Python List = %i\n", size);
    printf("[*] Allocated = %li\n", (long)list->allocated);
    for (i = 0; i < size; i++)
        printf("Element %i: %s\n", i, Py_TYPE(list->ob_item[i])->tp_name);
}
