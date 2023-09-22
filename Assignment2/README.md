# TODO Please edit the following information in your assignment

- Name: Derek Laister
- How many hours did it take you to complete this assignment? Too many...
- Did you collaborate with any other students/TAs/Professors? No
- Did you use any external resources? (Cite them below)
  - freeCodeCamp
  - youtube
  - stack overflow
  - python unittest documentation
- (Optional) What was your favorite part of the assignment? Creating a package (though not successful) to share project contents
- (Optional) How would you improve the assignment? A walk thorough with more detail on .gitignore explanation would be nice, and it would aslo be nice to have a more detailed walkthrough of the creation of the deliverable package since there are so many steps and it's not 100% clear on the overall work needed, where it goes, and how to submit. Lots of Documentation is great until you get lost in it because it is so much. Boiling down to the necessities would be a better use of time and then exploring further as needed. 

# Implementation Logistics

- You may use whatever operating system, IDE, or tools for completing this assignment.
- In the future there may be restrictions, so please review here.

# Part(s) to this assignment!

See the folders [part1](./part1) and [part2](./part2) for this assignment. **You should complete the assignment in order**

# Rubric

  <table>
  <tbody>
    <tr>
      <th>Points</th>
      <th align="center">Description</th>
    </tr>
      <td>50% (Part 1 - extend the json library to support complex and range objects)</td>
	        <td ><ul>
              <li>You must import the json standard library so that you can extend the json.JSONEncoder and json.JSONDecoder classes</li>
              <li>Read the Python [documentation](https://docs.python.org/3/library/json.html) for examples on how to serialize unsupported objects</li>
              <li>You must have tests that check if complex and range objects can be both serialized and deserialized</li>
            </ul></td>
    </tr>
  </tbody>
</table>

  <table>
  <tbody>
    <tr>
      <th>Points</th>
      <th align="center">Description</th>
    </tr>
	 <tr>
		<td>10% (Part 2) Publishing to Github</td>
		<td align="left"><ul>
            <li>Using your Github personal account, create a new, empty public repo named `jsonapi`</li>
              <li>When your work is finished, push your 'main' branch to that repo on Github</li>
              <li>Create a tag called 'v0.0.1' from the main branch on Github</li>
              <li>Create your first release notes using the tag; publish the release notes on Github</li>
        </ul></td>
	  </tr>
	<tr>
    	<td>40% (Part 2) Packaging and Distribution</td>
		<td align="left"><ul>
          <li>Create a setup.py</li>
          <li>Create a README.md that describes your repo, gives instructions on how to install it locally, and some code examples on how to use it</li>
          <li>Create a CHANGELOG.md</li>
          <li>Create a .gitignore</li>
          <li>Test your setup.py by building a source and wheel distribution locally. I.e. use python -m build, which should create a new dist/ folder containing the distribution files</li>
        </ul></td>
    </tr>
  </tbody>
</table>


* Note: You must also commit any additional files into your repository so we can test your code.
  * Points will be lost if you forget!
