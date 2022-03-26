<h3>For this project, you'll create a custom Soup() class that can take Ingredient() and Spice() objects, and use them to look up soup recipes on the Internet.</h3>

<p>Your Soup() objects should at least be able to:</p>

<p>take an unlimited number of Ingredient() or Spice() objects during instantiation</p>
<p>have a .cook() method that returns a search result for a soup recipe using all the added ingredients</p>
<p>Keep in mind that you're building an abstraction for your users. You can hide a lot of the inner workings of your Soup() instances from them to present them with a simple interface.</p>

<p>When you're done with this functionality, you can continue to extend this project in a couple of ways, for example:</p>

<p>take the amount of each Ingredient() into account. How can you work that into creating a recipe the user can actually cook?</p>
<p>interface with a recipe API instead of concatenating a web search URL. Receive the API response data, format it, and display it as command-line output.</p>
<p>create child classes to Soup() that have specific qualities.</p>
<p>You can make this project as complex and involved as you want to. However, keep thinking about it from a user's perspective, too. What abstraction would make sense to you? What functionality do you expect?</p>

<h2>Summary of this code</h2>

<h3>cook method in Soup Class</h3>
<p>Find 3 menues using the ingredients specified.</p>
<p>Then give you information of menu names, required amount of the specified ingredients, missing ingredients, photo of the meals if required(need to uncomment line 69)</p>
<br>
<h3>calory method in Information Class</h3>
<p>Find calory information as well as some nutrients information of those 3 meals.</p>
<br>
<h3>gulten method in Information Class</h3>
<p>Find gulten information for those 3 meals.</p>
