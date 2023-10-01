**TODO for your task:** Edit the Text in italics with your text.

<hr>

# Use Case 4

<hr>

**Use Case**: *Left click on mouse allows drawing on canvas.*

**Primary Actor**: *User.*

**Goal in Context**: *When the mouse is pressed and a user left-clicks (i.e. on the pressed event, not released) a pixel color will change wherever the mouse is located. This should allow me to drag and draw over the canvas like a pencil on a piece of paper.*

**Preconditions**: *conditions that must be true before the scenario may play out*

**Trigger**: *(1) Pressing the left button on the mouse. (2) Moving the mouse.*
  
**Scenario**: *The user will press the left mouse button and move the mouse to draw a shape.*
 
**Exceptions**: *CLick and hold outside of window canvas and then bring brush into the window canvas may cause unexpected behavior.*

**Priority**: *High-priority.*

**When available**: *First release*

**Channel to actor**: *The primary actor communicates through I/O devices. This includes the keyboard and the mouse. The system is responsible for maintaining focus of the window when the user clicks, and should respond within 1 second of any keyboard event. The user is responsible for all other input.*

**Secondary Actor**: *N/A.*

**Channels to Secondary Actors**: *N/A.*

**Open Issues**: *We may need to implement an exception for drawing outside the window canvas and for starting to draw out side the bounds but return to the canvas in a single action.*

<hr>



(adapted by Pressman and Maxim, Software Engineering: A Practitioner’s Approach, pp. 151-152, from Cockburn,
A., Writing Effective Use-Cases, Addison-Wesley, 2001)
