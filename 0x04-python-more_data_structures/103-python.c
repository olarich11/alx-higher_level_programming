#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - Prints bytes information
 *
 * @p: Python Object
 * Return: no return
 */
void print_python_bytes(PyObject *p)
{
    PyBytesObject *bytes_obj;
    unsigned char *bytes_data;
    Py_ssize_t size, limit, i;

    printf("[.] bytes object info\n");

    if (!PyBytes_Check(p))
    {
        printf("[ERROR] Invalid Bytes Object\n");
        return;
    }

    bytes_obj = (PyBytesObject *)p;
    bytes_data = (unsigned char *)PyBytes_AsString(p);
    size = PyBytes_Size(p);

    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", bytes_data);

    limit = size > 10 ? 10 : size;
    printf("  first %ld bytes:", limit);
    for (i = 0; i < limit; i++)
    {
        printf(" %02x", bytes_data[i]);
    }
    printf("\n");
}
