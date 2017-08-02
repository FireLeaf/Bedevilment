## Introduction ##

 eXtendedMirror is a reflection system for C++ with the following features:

- Compiler Independent
- Non intrusive
- No mandatory parser required
- Variant based interface
- Dry-est possible interface

It supports almost all the construct of the language (with some limitations) such as:

- Primitive Types
- Pointer Types
- References
- C Array Types
- Classes
- Multiple Inheritance
- Abstract Classes
- Methods
- Static Functions
- Namespaces
- Class Templates
- Constants
- Enumerators
- Static and Global Variables

You can find a lot of useful information in   [this](http://www.codeproject.com/Articles/1013256/An-Awful-Still-Useful-Cplusplus-Reflection-Syste) article.

## Dependencies ##

The code only depends on the c++11 standard library, but the build system depends on [CMake](http://www.cmake.org/) and [Python](https://www.python.org/)
To generate the documentation you need [Doxygen](http://www.doxygen.org/)

## Building ##

To build the library you first have to run CMake from the project directory


```
cmake -DCMAKE_BUILD_TYPE=Debug .
```


You can change Debug with Release if you want, and you can set some other parameters such as

- FUNC_PARAM_MAX: maximum number of supported function parameters (defaults to 8).
- GET_N_SET_EXTR_PARAM_MAX: Maximum number of supported extra parameters for getters and setters, that is the maximum number of parameters for getters, and the maximum number of parameters for setters, beyond the first (i.e. the value to set) (defaults to 3).
- TEMPL_PARAM_MAX: Maximum number of supported template parameters, for class templates (defaults to 4).

After running CMake, you can build the library and the tests by running


```
make
```
To install on your system type


```
make install
```

To build the documentation


```
make doc
```

## Using the library ##

To use the library include the header XM/xMirror.hpp in your compile units and link to the libxMirror library.
You can get more info [here](http://www.codeproject.com/Articles/1013256/An-Awful-Still-Useful-Cplusplus-Reflection-Syste) 
###MyClass.hpp###

```
#include<XM/xMirror.h>

class MyClass {
public:
    int myMethod(int a, int b);
    int myField;

    int getMyField2();
    void setMyField2(int val);

private:
    int myField2;
};
XM_DECLARE_CLASS(MyClass);
```
###MyClass.cpp###

```
// Methods definition here

XM_DEFINE_CLASS(MyClass)
{
    // Binds a method with automatic name extrapolation
    bindMethod(XM_MNP(myMethod));
  
    // Binds a property from a field
    bindProperty(XM_MNP(myField));

    // Binds a property from get and set methods
    bindProperty("myField2", &MyClass::getMyField2, &MyClass::setMyField2);
}

XM_REGISTER_TYPE(MyClass);
```


## Roadmap ##
- Reflect the standard library
- Primitive types casting
- Pointer to reference casting
- General Type casters
- Multiple constructors
- Parser (?)
