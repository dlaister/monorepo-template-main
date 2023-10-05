# TODO Please edit the following information in your assignment

- Name: Derek Laister
- How many hours did it take you to complete this assignment? 12 (likely more, as i'll forget to update this)
- Did you collaborate with any other students/TAs/Professors? No
- Did you use any external resources? (Cite them below)
  - Stack Overflow
  - Youtube
  - ChatGPT
  - A very helpful walkthrough by Joao Ortiz (explained [here](https://joaoortizz.medium.com/my-solution-for-the-gilded-rose-refactoring-kata-21e0338692cf)) was instrumental in understanding the "parts" of the assigment.
- (Optional) What was your favorite part of the assignment? It was fun trying to figure out how to solve the Gilded Rose Problem, but I am not very good as a software developer to know the means to solve. Testing is one thing, not my favorite nor am I very knowledgeable in it, but it was at least fun trying to get things to work and figure out the best course of action to take. Ortiz (a used resource) helped me navigate and think about the design patterns. I went through the list of different patterns to see what I would come up with but none of them really popped out at me until I started fumbling around seeing what could be done. When I was lost, I had Ortiz to reference. When walking through, I noticed a Factory pattern immerge (which made sense after realizing you want to work with different objects of a similar type, work with their attributes, and allow expansion off a root class). I also noticed a hint of Builder pattern (thought I think im a bit confused on it). But, since there are "Items", and they are broken into different representations (different sell_in and quality attributes). 
- (Optional) How would you improve the assignment? That's a hard one. Testing was stressed as a way to start this assignment, but testing is not my strong suit so, I'd say there must be points of entry elsewhere into the solution. Another thing I tend to get lost in are the external links that are sometimes helpful, but often times distracting. It might be a nice add to specify if they are needed for the assignment or if they are supplemental but not needed for the task to be completed. The TextTest portion leads me to believe it was required but the rubric does not say this (though it is stated later that it is to help, and it is also from teh original Kata for the problem). A lot of thought and back peddling went into this and washing around. Yes, this is a age old problem in the CS realm, but a structured way to solve this would have been nice, and bonus points could have come from further researcha nd application. It just felt like there were a lot of ways to go for this problem which lead (at least me) down a few roads of try fail, restart, try and fail. 

# Implementation Logistics

- You may use whatever operating system, IDE, or tools for completing this assignment.
- In the future there may be restrictions, so please review here.

# Part(s) to this assignment!

See the folders [part1](./part1) for this assignment.

# Rubric
 
  <table>
  <tbody>
    <tr>
      <th>Points</th>
      <th align="center">Description</th>
    </tr>
    <tr>
      <td>10% (Housekeeping)</td>
	    <td align="left"><ul><li>If necessary, Update your .gitignore to avoid saving any unnecessary files such as python cache files or the dreadful .DS_Store. Ensure that only the three given Python modules and README.md are saved. If you don't have to update your .gitignore after doing the work, that is ok.</li></ul></td>
    </tr>
    <tr>
      <td>20% (Testing)</td>
	    <td align="left"><ul><li>Update tests to cover all the potential use cases</li></ul></td>
    </tr>
    <tr>
      <td>70% (Refactor)</td>
	    <td align="left"><ul><li>(10%) Do all the python modules work? I.e. Can you run each python module on the command line successfully?</li><li>(20%) Did you ensure NOT to change the Item class or Items attribute?</li><li>(20%)Did you implement all the required changes per the spec?</li><li>(20%)Did you refactor the code for readability and maintainability?</li><li>We will not grade for 'performance' in this assignment</li><li>(30%) Did you apply any design patterns to refactor and improve the design of the GildedRose class?</li></ul></td>
    </tr>	  
  </tbody>
</table>

* Note: You must also commit any additional files into your repository so we can test your code.
  * Points will be lost if you forget!
