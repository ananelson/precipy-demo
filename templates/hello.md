<style>
    @page {
        size: letter landscape;
        margin: 2cm;
    }
</style>

## Welcome

This is some text.

Here is a video image;

<video controls="controls" width="800" height="600" name="Video Name">
   <source src="/Users/ana/dev/precipy/demo/file_example_MOV_480_700kB.mov">
    Video tag not supported.
</video>

Here is a list of keys:
{% for k in keys %}
### {{ k }}

{% if data[k].files is defined %}
{% for cn, info in data[k].files.items() %}
- {{ cn  }}
{% for kk, vv in info.items() -%}
     - {{ kk }}: {{ vv }}
{% endfor -%}
{% if data[k].files[cn]['url'].endswith(".png") %}
![Plot]({{ data[k].files[cn]['url'] }})
{% endif %}
{% endfor %}
{% endif %}


{% endfor %}

