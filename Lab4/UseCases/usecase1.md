**TODO for your task:** Edit the Text in italics with your text.

<hr>

# Use Case 1

<hr>

**Use Case**: *New Program Window.*

**Primary Actor**: *User.*

**Goal in Context**: *To create a new window and drawable canvas 600x400 (600 pixels wide, 400 pixels high).*

**Preconditions**: *The program must be opened.*

**Trigger**: *(1) Application must be opened. (2) Create a new widow if option is available.*
  
**Scenario**: *User will open the application from the applications list or dock. Application will open a new window and canvas in desired size.*
 
**Exceptions**: *New window already opened, user will be prompted to either continue or create a new window.*

**Priority**: *High-priority.*

**When available**: *First release.*

**Channel to actor**: *The primary actor is the system which is responsible for allocating resources to create a new instance of the application with the desired specifications.*

**Secondary Actor**: *The secondary actor (user) communicates through I/O devices. This includes the keyboard and the mouse. The system is responsible for maintaining focus of the window when the user clicks, and should respond within 1 second of any keyboard event. The user is responsible for all other input.*

**Channels to Secondary Actors**: *The secondary actor may interact through I/O devices such as a mouse, keyboard, touchpad, or stylus.*

**Open Issues**: *Window may need a default behavior, such as it opens in white. The user can be prompted in a future relase as what to do with the background on open. This may be a user set setting, or can be set per instance.*

<hr>



(adapted by Pressman and Maxim, Software Engineering: A Practitioner’s Approach, pp. 151-152, from Cockburn,
A., Writing Effective Use-Cases, Addison-Wesley, 2001)
