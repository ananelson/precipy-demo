<style>
    @page {
        size: letter landscape;
        margin: 2cm;
    }
</style>

## General

Templates can be written in any markup language. Markdown is a common choice.

Template tags use Jinja2 syntax. Here is Jinja's [template designer documentation](https://jinja.palletsprojects.com/en/2.11.x/templates/) page.

## Environment

Precipy populates the jinja environment with information from analytics functions, and about the batch as a whole.

### Constants

If there are any constants defined in the config, they are accessible via the `constants` dictionary or directly in the top level namespace.

<table>

</table>

### Functions

The `functions` top-level object contains a dictionary of AnalyticsFunctions objects, keyed by function key.

For this demo, the analytics functions are:


- hello

Each of these function keys can also be used directly. Let's look at the attributes/methods available for one of these function objects in detail.



#### hello

`function_name` attribute:
hello

`function_elapsed_seconds` attribute:
The function took 6.9141387939453125e-06 seconds to run.

`function_source` attribute, with `highlight` filter applied:
<pre>
<div class="highlight" style="background: #f8f8f8"><pre style="line-height: 125%"><span></span><a name="l-1"></a><span style="color: #008000; font-weight: bold">def</span> <span style="color: #0000FF">hello</span>(af):
<a name="l-2"></a>    <span style="color: #008000; font-weight: bold">return</span> <span style="color: #666666">-1</span>
</pre></div>
</pre>

`function_output` attribute:
The function returned output: `-1`

The `kwargs` attribute contains function arguments in a dictionary:



The `files` attribute contains all files associated with this function in a dictionary. Usually these are the files generated as side effects from running the function:


- metadata.pkl 