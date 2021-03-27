#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdio.h>
#include <iostream>

int Ccompter(int n)
{
	int c = 0;
	for(int i =0; i< n; i++)
	{
		c += 1;	
	}
	return c;
}

int CgetArray()
{

	srand(time(NULL));
	int c = 0;
	for (int i = 0; i < 1000000; i++)
	{
		int random2 = rand() % 10;
		c += random2;
	}

	return c;
}

//note :  METH_VARARGS signifie qu'on envoie un tupe d'argmuent dans args qu'il faut parser avec PyArg_ParseTUple pour pouvoir le lire
static PyObject* getArray(PyObject* self, PyObject* args) 
{
	//int s = PyTuple_Size(arr);


	int *tab = new int[3];
	
	PyObject* arr;

	if (!PyArg_ParseTuple(args, "O", &arr))
		return NULL;


	int k = 0;
	for (int i = 0; i < 3; i++) {

		
		PyObject* value = PyList_GetItem(arr, i);
		//data.push_back(Py_BuildValue("i", value));
		tab[i] = (int) PyLong_AsLong(value) + 1;
	}
	

	/*PyObject *result = PyList_New(5);
	int * c = CgetArray();
	PyList_SetItem(result, 0,Py_BuildValue("i",c[0]));
	PyList_SetItem(result, 1,Py_BuildValue("i",c[1]));
	PyList_SetItem(result, 2,Py_BuildValue("i",c[2]));
	PyList_SetItem(result, 3,Py_BuildValue("i",c[3]));
	PyList_SetItem(result, 4,Py_BuildValue("i",c[4]));*/
	PyObject* result = PyList_New(3);


	PyList_SetItem(result, 0, Py_BuildValue("i", tab[0]));
	PyList_SetItem(result, 1, Py_BuildValue("i", tab[1]));
	PyList_SetItem(result, 2, Py_BuildValue("i", tab[2]));



	return result;

	//return Py_BuildValue("i",CgetArray());
	
}


static PyMethodDef myMethods[] = {
	{"getArray",getArray,METH_VARARGS,"LMAO"},
	{NULL,NULL,0,NULL}
};

static struct PyModuleDef myModule = {
	PyModuleDef_HEAD_INIT,
	"myModule",
	"Comper module",
	-1,
	myMethods
};

PyMODINIT_FUNC PyInit_myModule(void)
{
	return PyModule_Create(&myModule);
}
