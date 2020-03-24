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

{% for const, value in constants.items() %}
- {{ const }} = {{ value }}{% endfor %}

### Functions

The `functions` top-level object contains a dictionary of AnalyticsFunctions objects, keyed by function key.

For this demo, the analytics functions are:

{% for key, af in functions.items() %}
- {{ key }}{% endfor %}

Each of these function keys can also be used directly. Let's look at the attributes/methods available for one of these function objects in detail.

{% set af = plot_values %}

#### {{ af.key }}

`function_name` attribute:
{{ af.function_name }}

`function_elapsed_seconds` attribute:
The function took {{ af.function_elapsed_seconds }} seconds to run.

`function_source` attribute, with `highlight` filter applied:
<pre>
{{ af.function_source | highlight }}</pre>

`function_output` attribute:
The function returned output: `{{ af.function_output }}`

The `kwargs` attribute contains function arguments in a dictionary:

{% for k, v in af.kwargs.items() %}
- {{ k }}: {{ v }}{% endfor %}

The `files` attribute contains all files associated with this function in a dictionary. Usually these are the files generated as side effects from running the function:

{% for k in af.files.keys() %}
- {{ k }} {{ v }}{% endfor %}

### Files

Let's look at the attributes available for a `files` instance.

Canonical Filename: {{ af.files[PLOT_FILENAME].canonical_filename }}

Cache Filepath: {{ af.files[PLOT_FILENAME].cache_filepath }}

Public URLs: {{ af.files[PLOT_FILENAME].public_urls }}

Depending on the use case, you may wish to link to assets in the output directory (which will be the same directory where documentation will end up. Or the cache filepath, which will be a fully qualified path on the same file system. Or one of the Public URLs which show where the item has been uploaded to cloud storage. (Bucket must be sent to public/anonymous access.)

Here are examples of img tages using each of these three.

<img src="{{ af.files[PLOT_FILENAME].canonical_filename }}" style="border: thin solid grey; width: 200px;" width="200px"></img>
<img src="{{ af.files[PLOT_FILENAME].cache_filepath }}"  style="border: thin solid blue; width: 200px;"></img>
<img src="{{ af.files[PLOT_FILENAME].public_urls[0] }}"  style="border: thin solid red; width: 200px;"></img>


