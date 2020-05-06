#include <Python.h>

/**
  * print_python_list_info - print python list info
  * @p: pointer for PyObject
  * Return: N/A
  */

void print_python_list_info(PyObject *p)
{
	Py_ssize_t size_p, allocated, idex = 0;

	PyObject *item;

	size_p = PyList_Size(p);

	allocated = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %ld\n", size_p);

	printf("[*] Allocated = %ld\n", allocated);

	while (idex < size_p)
	{
		item = PyList_GET_ITEM(p, idex);

		printf("Element %ld: %s\n", idex, item->ob_type->tp_name);
		idex++;
	}
}
