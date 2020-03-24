<style>
    @page {
        size: letter landscape;
        margin: 2cm;
    }
</style>

## General

Templates can be written in any markup language. Markdown is a common choice.

Template tags use Jinja2 syntax. Here is the "template designer documentation":https://jinja.palletsprojects.com/en/2.11.x/templates/ page.

## Environment

Precipy populates the jinja environment with information from analytics functions, and about the batch as a whole.

### Constants

If there are any constants defined in the config, they are accessible via the `constants` dictionary or directly in the top level namespace.


- RANDOM_FILENAME = random_0_100.npy
- PLOT_FILENAME = plot_with_overlay.png

### Functions

The `functions` top-level object contains a dictionary of AnalyticsFunctions objects, keyed by function key.

For this demo, the analytics functions are:


- write_data_file_without_object
- read_data_file_without_object
- generate_data
- generate_data_1000
- plot_values

Each of these function keys can also be used directly. Let's look at the attributes/methods available for one of these function objects in detail.



#### plot_values

`function_name` attribute:
<bound method AnalyticsFunction.function_name of <precipy.analytics_function.AnalyticsFunction object at 0x11a264cc0>>

`function_elapsed_seconds` attribute:
The function took 0.5163979530334473 seconds to run.

`function_source` attribute, with `highlight` filter applied:
<pre>
<div class="highlight" style="background: #f8f8f8"><pre style="line-height: 125%"><span></span><a name="l-1"></a><span style="color: #666666">&lt;</span>bound method AnalyticsFunction<span style="color: #666666">.</span>function_source of <span style="color: #666666">&lt;</span>precipy<span style="color: #666666">.</span>analytics_function<span style="color: #666666">.</span>AnalyticsFunction <span style="color: #008000">object</span> at <span style="color: #666666">0x11a264cc0&gt;&gt;</span>
</pre></div>
</pre>

`function_output` attribute:
The function returned output: `None`

The `kwargs` attribute contains function arguments in a dictionary:


- c: 40
- n: 10

The `files` attribute contains all files associated with this function in a dictionary. Usually these are the files generated as side effects from running the function:


- metadata.pkl 
- plot_with_overlay.png 

### Files

Let's look at the attributes available for a `files` instance.

Canonical Filename: plot_with_overlay.png

Cache Filepath: /var/folders/wb/1y3rpg4n7798b3nxxlj6vdy80000gn/T/precipy/precipy_demo_cache/e6/e6ec5e651a4ef84f9bb315640a3711223b6786d5f2ec36af2ab383776a457798.png

Public URLs: ['https://storage.googleapis.com/precipy_demo_cache/e6ec5e651a4ef84f9bb315640a3711223b6786d5f2ec36af2ab383776a457798.png']

Depending on the use case, you may wish to link to assets in the output directory (which will be the same directory where documentation will end up. Or the cache filepath, which will be a fully qualified path on the same file system. Or one of the Public URLs which show where the item has been uploaded to cloud storage. (Bucket must be sent to public/anonymous access.)

Here are examples of img tages using each of these three.

<img src="plot_with_overlay.png" width="200px"></img>
<img src="/var/folders/wb/1y3rpg4n7798b3nxxlj6vdy80000gn/T/precipy/precipy_demo_cache/e6/e6ec5e651a4ef84f9bb315640a3711223b6786d5f2ec36af2ab383776a457798.png"  style="border: thin solid blue; width: 200px;"></img>
<img src="https://storage.googleapis.com/precipy_demo_cache/e6ec5e651a4ef84f9bb315640a3711223b6786d5f2ec36af2ab383776a457798.png"  style="border: thin solid red; width: 200px;"></img>

