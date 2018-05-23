---
layout: default
---

# Ziknet-Trends

Ziknet-Trends is a project developed at ITESM which attempts to develop a model to predict Zika virus epidemics using online information retrieved from health organizations and Google Trends and LSTM networks.

<!-- Text can be **bold**, _italic_, or ~~strikethrough~~.

[Link to another page](./another-page.html).

There should be whitespace between paragraphs.

There should be whitespace between paragraphs. We recommend including a README, or a file with information about your project.
 -->
# Why LSTM Networks?

This is a normal paragraph following a header. GitHub is a code hosting platform for version control and collaboration. It lets you and others work together on projects from anywhere.

<script src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.1.10/require.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/2.0.3/jquery.min.js"></script>

<div id="graph-cb5e7954-9c20-4141-9a18-6c8d1b4a19a8"></div>
  <script type="text/javascript">
           require.config({baseUrl: '/',
                             paths: {jgraph: ['nbextensions/jgraph.min', 'https://rawgit.com/patrickfuller/jgraph/master/js/build/jgraph.min']}});
           require(['jgraph'], function () {
               var $d = $('#graph-cb5e7954-9c20-4141-9a18-6c8d1b4a19a8');
               $d.width(600); $d.height(400);
               $d.jgraph = jQuery.extend({}, jgraph);
               $d.jgraph.create($d, {nodeSize: 2.000000,
                                     edgeSize: 0.250000,
                                     defaultNodeColor: '0x5bc0de',
                                     defaultEdgeColor: '0xaaaaaa',
                                     shader: 'basic',
                                     z: 200,
                                     runOptimization: true,
                                     directed: true,
                                     showSave: false});
               $d.jgraph.draw({
    "edges": [
        { "color": "0x0", "source": "bn", "target": "ah" },
        { "color": "0x0", "source": "bn", "target": "cb" },
        { "color": "0x0", "source": "bv", "target": "bw" },
        { "color": "0x0", "source": "bv", "target": "cg" },
        { "color": "0x0", "source": "cc", "target": "cj" },
        { "color": "0x0", "source": "cj", "target": "ag" },
        { "color": "0x0", "source": "ck", "target": "bn" },
        { "color": "0x0", "source": "ck", "target": "bc" },
        { "color": "0x0", "source": "ck", "target": "bv" },
        { "color": "0x0", "source": "ck", "target": "ai" },
        { "color": "0x0", "source": "ck", "target": "by" },
        { "color": "0x0", "source": "bn", "target": "ah" },
        { "color": "0x0", "source": "bn", "target": "cb" },
        { "color": "0x0", "source": "bv", "target": "bw" },
        { "color": "0x0", "source": "bv", "target": "cg" },
        { "color": "0x0", "source": "cc", "target": "cj" },
        { "color": "0x0", "source": "cj", "target": "ag" },
        { "color": "0x0", "source": "ck", "target": "bn" },
        { "color": "0x0", "source": "ck", "target": "bc" },
        { "color": "0x0", "source": "ck", "target": "bv" },
        { "color": "0x0", "source": "ck", "target": "ai" },
        { "color": "0x0", "source": "ck", "target": "by" },
        { "color": "0x0", "source": "bn", "target": "ah" },
        { "color": "0x0", "source": "bn", "target": "cb" },
        { "color": "0x0", "source": "bv", "target": "bw" },
        { "color": "0x0", "source": "bv", "target": "cg" },
        { "color": "0x0", "source": "cc", "target": "cj" },
        { "color": "0x0", "source": "cj", "target": "ag" },
        { "color": "0x0", "source": "ck", "target": "bn" },
        { "color": "0x0", "source": "ck", "target": "bc" },
        { "color": "0x0", "source": "ck", "target": "bv" },
        { "color": "0x0", "source": "ck", "target": "ai" },
        { "color": "0x0", "source": "ck", "target": "by" }
    ],
    "nodes": {
        "aa": { "color": "0xc853", "size": 2.0 },
        "ab": { "color": "0xc853", "size": 2.0 },
        "ac": { "color": "0xc853", "size": 2.0 },
        "ad": { "color": "0xc853", "size": 2.0 },
        "ae": { "color": "0xc853", "size": 2.0 },
        "af": { "color": "0xc853", "size": 2.0 },
        "ag": { "color": "0x2962ff", "size": 2.0 },
        "ah": { "color": "0x2962ff", "size": 2.0 },
        "ai": { "color": "0x2962ff", "size": 2.0 },
        "aj": { "color": "0xc853", "size": 2.0 },
        "ak": { "color": "0xc853", "size": 2.0 },
        "al": { "color": "0xc853", "size": 2.0 },
        "am": { "color": "0xc853", "size": 2.0 },
        "an": { "color": "0xc853", "size": 2.0 },
        "ao": { "color": "0xc853", "size": 2.0 },
        "ap": { "color": "0xc853", "size": 2.0 },
        "aq": { "color": "0xc853", "size": 2.0 },
        "ar": { "color": "0xc853", "size": 2.0 },
        "as": { "color": "0xc853", "size": 2.0 },
        "at": { "color": "0xc853", "size": 2.0 },
        "au": { "color": "0xc853", "size": 2.0 },
        "av": { "color": "0xc853", "size": 2.0 },
        "aw": { "color": "0x2962ff", "size": 2.0 },
        "ax": { "color": "0xc853", "size": 2.0 },
        "ay": { "color": "0xc853", "size": 2.0 },
        "ba": { "color": "0xc853", "size": 2.0 },
        "bb": { "color": "0xc853", "size": 2.0 },
        "bc": { "color": "0x2962ff", "size": 2.0 },
        "bd": { "color": "0xc853", "size": 2.0 },
        "be": { "color": "0xc853", "size": 2.0 },
        "bf": { "color": "0xc853", "size": 2.0 },
        "bg": { "color": "0xc853", "size": 2.0 },
        "bh": { "color": "0xc853", "size": 2.0 },
        "bi": { "color": "0xc853", "size": 2.0 },
        "bj": { "color": "0xc853", "size": 2.0 },
        "bk": { "color": "0xc853", "size": 2.0 },
        "bl": { "color": "0xc853", "size": 2.0 },
        "bm": { "color": "0xc853", "size": 2.0 },
        "bn": { "color": "0x2962ff", "size": 2.0 },
        "bo": { "color": "0xc853", "size": 2.0 },
        "bp": { "color": "0xc853", "size": 2.0 },
        "bq": { "color": "0xc853", "size": 2.0 },
        "br": { "color": "0xc853", "size": 2.0 },
        "bs": { "color": "0xc853", "size": 2.0 },
        "bt": { "color": "0xc853", "size": 2.0 },
        "bu": { "color": "0xc853", "size": 2.0 },
        "bv": { "color": "0x2962ff", "size": 2.0 },
        "bw": { "color": "0x2962ff", "size": 2.0 },
        "bx": { "color": "0xc853", "size": 2.0 },
        "by": { "color": "0x2962ff", "size": 2.0 },
        "bz": { "color": "0xc853", "size": 2.0 },
        "ca": { "color": "0xc853", "size": 2.0 },
        "cb": { "color": "0xf57f17", "size": 2.0 },
        "cc": { "color": "0x2962ff", "size": 2.0 },
        "cd": { "color": "0xc853", "size": 2.0 },
        "ce": { "color": "0xc853", "size": 2.0 },
        "cf": { "color": "0xc853", "size": 2.0 },
        "cg": { "color": "0xd50000", "size": 2.0 },
        "ch": { "color": "0xc853", "size": 2.0 },
        "ci": { "color": "0xc853", "size": 2.0 },
        "cj": { "color": "0x2962ff", "size": 2.0 },
        "ck": { "color": "0x2962ff", "size": 2.0 }
    }
});

               $d.resizable({
                   aspectRatio: 600 / 400,
                   resize: function (evt, ui) {
                       $d.jgraph.renderer.setSize(ui.size.width,
                                                  ui.size.height);
                   }
               });
           });
  </script>

<a href="Graph.html">LINK</a>

## Header 2

> This is a blockquote following a header.
>
> When something is important enough, you do it even if the odds are not in your favor.

### Header 3

```js
// Javascript code with syntax highlighting.
var fun = function lang(l) {
  dateformat.i18n = require('./lang/' + l)
  return true;
}
```

```ruby
# Ruby code with syntax highlighting
GitHubPages::Dependencies.gems.each do |gem, version|
  s.add_dependency(gem, "= #{version}")
end
```

#### Header 4

*   This is an unordered list following a header.
*   This is an unordered list following a header.
*   This is an unordered list following a header.

##### Header 5

1.  This is an ordered list following a header.
2.  This is an ordered list following a header.
3.  This is an ordered list following a header.

###### Header 6

| head1        | head two          | three |
|:-------------|:------------------|:------|
| ok           | good swedish fish | nice  |
| out of stock | good and plenty   | nice  |
| ok           | good `oreos`      | hmm   |
| ok           | good `zoute` drop | yumm  |

### There's a horizontal rule below this.

* * *

### Here is an unordered list:

*   Item foo
*   Item bar
*   Item baz
*   Item zip

### And an ordered list:

1.  Item one
1.  Item two
1.  Item three
1.  Item four

### And a nested list:

- level 1 item
  - level 2 item
  - level 2 item
    - level 3 item
    - level 3 item
- level 1 item
  - level 2 item
  - level 2 item
  - level 2 item
- level 1 item
  - level 2 item
  - level 2 item
- level 1 item

### Small image

![Octocat](https://assets-cdn.github.com/images/icons/emoji/octocat.png)

### Large image

![Branching](https://guides.github.com/activities/hello-world/branching.png)


### Definition lists can be used with HTML syntax.

<dl>
<dt>Name</dt>
<dd>Godzilla</dd>
<dt>Born</dt>
<dd>1952</dd>
<dt>Birthplace</dt>
<dd>Japan</dd>
<dt>Color</dt>
<dd>Green</dd>
</dl>

```
Long, single-line code blocks should not wrap. They should horizontally scroll if they are too long. This line should be long enough to demonstrate this.
```

```
The final element.
```
