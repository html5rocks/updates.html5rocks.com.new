This is work in progress. 

A stub for jekyll-based version of updates.html5rocks.com site.

## Get the code

    git clone https://github.com/html5rocks/updates.html5rocks.com.new.git --recursive

The recursive option allows you to checkout the /samples submodule,
which points to
[github.com/GoogleChrome/samples](https://github.com/GoogleChrome/samples).

## Run it locally

Make sure you have `ruby` and `jekyll` installed:
[jekyllrb.com](http://jekyllrb.com/). Then run:

    jekyll serve --watch
    
## Create a new post

Updates.html5rocks.com is all about fresh content, so that means you need to post to it.  

*  Create a file in _posts/
*  Name the file in the following format  YYYY-MM-DD-SOME-TEXT-NAME.md
*  Add a Yaml header (use the template below - NOTE change every field)
*  Write your content.

```
---
layout: post
title: "Getting Literal With ES6 Template Strings"
description: "Template String literals with embedded expressions. We've been waiting for this for ages. Literally"
article:
  written_on: 2015-01-20
  updated_on: 2015-01-20
authors:
  - addyosmani
tags:
  - es6
  - javascript
  - ecmascript
permalink: /2015/01/ES6-Template-Strings
---
```

## Getting your post live.

*  Commit to development branch, or file a PR to the project
*  Ask someone to test locally, and then get them to merge to master.

## Include samples

Including samples into posts is done via the `include_code` plugin
(a modified version of
[Web Fundamentals code_include](https://github.com/google/WebFundamentals/blob/master/src/site/_plugins/include_code.rb)). It assumes that the samples are stored in
`/samples` directory, each in  its own folder, with `index.html`
file as the main sample file.
Sample file has to have named sections for each
includable code snippet, e.g.:

    <!-- // [START name-of-this-snippet] -->
    <p>This is the code I want to include as a sample snippet</p>
    <!-- // [END name-of-this-snippet] -->

To include a sample, use `include_code` tag in your post:

    {% include_code <sample-dir> <snippet-name> %}

e.g.

    {% include_code css-shapes shape-outside-polygon %}
