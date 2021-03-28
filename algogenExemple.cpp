#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <deque>
//#include <algogen.h>

int Calgogen(int n)
{
	int c = 0;
	for (int i = 0; i < n; i++)
		c++;
	return c;
}


static PyObject* algogen(PyObject* self, PyObject* args)
{
	int n;
	if(!PyArg_ParseTuple(args, "i", &n))
		return NULL;
	return Py_BuildValue("i", Calgogen(n));
	
}


static PyMethodDef myMethods[] = {
	{"algogen",algogen,METH_VARARGS,"compte putain de merde"},
	{NULL,NULL,0,NULL}
};

static struct PyModuleDef genalgo = {
	PyModuleDef_HEAD_INIT,
	"genalgo",
	"genetic algo module",
	-1,
	myMethods
};

PyMODINIT_FUNC PyInit_algogen(void)
{
	return PyModule_Create(&genalgo);
}
