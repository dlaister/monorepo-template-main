# Exercises

Update your answers to the following questions, make sure to commit this file and your improved code as well!


## Task 1 - oop.py

1. Is MObject an abstract or a concrete class? Explain why:
	- *It appears that MObject is a CONCRETE class as it does not use the abc module and because it contains no implementable methods beyond itself. Furthermore, by default, Python does not provide a abstract classes per GeeksforGeeks. Python does however, come with a module that defines a base abstract class.*
1. The 'Image' class has commented code for a `__del__` method. What does this commented-out method do?
	- *__del__ is a destructor, and destroys the instance of. In this case, Image. In layman's terms, this destroys the object when it si no longer needed freeing up resource memory.*
1. What class does Texture inherit from?
	- *Texture inherits from the Image class as shown in the signature: class Texture(Image):*
1. What methods and attributes does the Texture class inherit from 'Image'? 
	- *The texture class inherits the following methods:
    	- *__init__(self, w, h)*
        - *getWidth(self)*
        - *getHeight(self)*
        - *getPixelColorR(self, x, y)*
        - *getPixels(self)*
        - *setPixelsToRandomValues(self)*
    - *The texture class inherits the following attributes(functions):
        - *m_Width*
        - *m_Height*
        - *m_PixelColorR*
        - *m_Pixels*
1. Do you think a texture should have a 'has-a' (composition) or 'is-a'(inheritance) relationship with 'Image'? If you think it is a 'has-a' relationship, refactor the code. As long as you defend your decision in the response below it could be either--but defend your position well!
	- *As pointed out in the prior question, the Texture class inherits from the Image class thus I would agree that Texture is-a Image. To me, this is a like a square that can be a rectangle, but not the other way around. Furthermore, an Image can have a texture where the concept of texture having an image does not make logical sense (at least to me).*
1. I did not declare a constructor for Texture. Does Python automatically create constructors for us? 
	- *Yes, Python WILL use a default constructor (a default __init__) if one is not provided though I am not sure it "creates" this - however rather than calling it from elsewhere.*

## Task 2 - Singleton

1. Refactor the singleton.py file such that:
  - The first time the logger is constructed, it will print out:
  	-  `Logger created exactly once`
  - If the logger is already initialized, it will print:
  	-  `logger already created`
Note: You do not 'have' a constructor, but you construct the object in the *instance* member function where you will create an object.  
Hint: Look at Lecture 3 slides for an example of creating a Singleton in Python

1. Are singleton's in Python thread safe? Why or why not?

*edit the code directly*  
  
