<h1>PySearching - Automated URL Opener</h1>
<p>PySearching is a Python application that automates the process of opening URLs from a text file using Selenium WebDriver and displays the current state in a GUI built with PySimpleGUI. This README will guide you through the setup and usage of the application.</p>

<h2>Features</h2>
<ul>
    <li>Automated URL opening using Selenium WebDriver</li>
    <li>Headless browsing mode</li>
    <li>Simple GUI for controlling the process</li>
    <li>Multi-threading for smooth GUI operation</li>
</ul>

<h2>Prerequisites</h2>
<ul>
    <li>Python 3.x</li>
    <li><code>selenium</code> library</li>
    <li><code>PySimpleGUI</code> library</li>
    <li><code>chromedriver</code> (compatible with your installed version of Chrome)</li>
</ul>

<h2>Installation</h2>
<p>Install the required libraries using pip:</p>
<pre><code>pip install selenium pysimplegui</code></pre>

<h2>Usage</h2>
<p>Create a text file named <code>websites.txt</code> in the same directory as the script. Add the URLs you want to open, each on a new line.</p>

<h3>Running the Script</h3>
<p>To run the script, execute the following command:</p>
<pre><code>python main.py</code></pre>

<h2>GUI Overview</h2>
<ul>
    <li><strong>ON Button</strong>: Starts the URL opening process.</li>
    <li><strong>OFF Button</strong>: Stops the URL opening process.</li>
    <li><strong>EDIT Button</strong>: Opens the <code>websites.txt</code> file for editing (not implemented in the script).</li>
    <li><strong>Status Text</strong>: Displays the current state of the process (ON/OFF).</li>
    <li><strong>Link Counter</strong>: Displays the number of links opened.</li>
</ul>

<h2>Code Overview</h2>
<p>The script uses Selenium WebDriver for browsing and PySimpleGUI for the graphical interface. It runs the URL opening process in a separate thread to keep the GUI responsive.</p>

<h2>Creating an Executable</h2>
<p>To create a standalone executable using PyInstaller, use the following command:</p>
<pre><code>pyinstaller --onefile --add-data "websites.txt;." --noconsole main.py</code></pre>

<h2>Contributing</h2>
<p>Feel free to fork this repository and submit pull requests if you have any improvements or bug fixes.</p>

<h2>License</h2>
<p>This project is licensed under the MIT License. See the LICENSE file for details.</p>

<hr>
<p>Thank you for using PySearching! If you have any questions or issues, please feel free to contact us.</p>
