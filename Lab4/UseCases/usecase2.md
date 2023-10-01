**TODO for your task:** Edit the Text in italics with your text.

<hr>

# Use Case 2

<hr>

**Use Case**: *Number Key Color Selection.*

**Primary Actor**: *User.*

**Goal in Context**: *Pressing the number keys 1 through 8 allows you to draw (fill) in a different color The key and corresponding colors are as follows:*
- 1 = Black
- 2 = White
- 3 = Red
- 4 = Green
- 5 = Blue
- 6 = Yellow
- 7 = Magenta
- 8 = Cyan

**Preconditions**: *Use Case 1 completed, a new program window has been created.*

**Trigger**: *Pressing any of the number keys 1 through 8 changes the window canvas to a desired corresponding color.*
  
**Scenario 1**: *The user will press number key 1 and the window canvas will draw (fill) in the color of Black.*

**Scenario 2**: *The user will press number key 2 and the window canvas will draw (fill) in the color of White.*

**Scenario 3**: *The user will press number key 3 and the window canvas will draw (fill) in the color of Red.*

**Scenario 4**: *The user will press number key 4 and the window canvas will draw (fill) in the color of Green.*

**Scenario 5**: *The user will press number key 5 and the window canvas will draw (fill) in the color of Blue.*

**Scenario 6**: *The user will press number key 6 and the window canvas will draw (fill) in the color of Yellow.*

**Scenario 7**: *The user will press number key 7 and the window canvas will draw (fill) in the color of Magenta.*

**Scenario 8**: *The user will press number key 8 and the window canvas will draw (fill) in the color of Cyan.*

**Exceptions**: *The program will respond with an error if the input is not number keys 1 through 8. In this case, the user will be prompted to enter a valid number key 1 through 8 or prompted to terminate (see Use Case 5).*

**Priority**: *High-priority.*

**When available**: *First release.*

**Channel to actor**: *The primary actor communicates through I/O devices. This includes the keyboard and the mouse. The system is responsible for maintaining focus of the window when the user clicks, and should respond within 1 second of any keyboard event. The user is responsible for all other input.*

**Secondary Actor**: *Mini-paint will respond to unintended input with an error and prompt the user to enter an appropriate response or ask to terminate (see Use Case 5).*

**Channels to Secondary Actors**: *In the event of an error or incorrect input value, Mini-paint will prompt the user with a dialog box with corrective actions.*

**Open Issues**: *Exception handling to address all edge-cases.*

<hr>



(adapted by Pressman and Maxim, Software Engineering: A Practitioner’s Approach, pp. 151-152, from Cockburn,
A., Writing Effective Use-Cases, Addison-Wesley, 2001)
