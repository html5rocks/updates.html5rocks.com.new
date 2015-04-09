---
layout: post
title: "DOM Attributes now on the prototype chain"
description: ""
article:
  written_on: 2015-04-09
  updated_on: 2015-04-09
authors:
  - paulkinlan
tags:
  - DOM
  - API change
permalink: /2015/04/DOM-attributes-now-on-the-prototype
---

The Chrome team recently [announced that we are moving DOM attributes to the prototype chain](https://groups.google.com/a/chromium.org/forum/#!topic/blink-dev/H0MGw0jkdn4).  This change, implemented in Chrome 43, brings Chrome inline with the spec and other browsers’ implementations, such as IE and Firefox.  WebKit based browsers, such as Safari, are currently not compatible with the spec. 

The new behavior is positive in many ways. It:

* Improves compatibility across the web (IE and Firefox do this already) via compliance with the spec.
* Allows you to efficiently create getters/setters on every DOM object. 
* Increases the hackability of DOM programming. For example, it will enable you to implement Polyfills that allow you to efficiently emulate functionality missing in some browsers and JavaScript libraries that override default DOM attribute behaviors. 

It can however cause some issues for developers, especially if you were relying on this behaviour because of legacy compatibility between Chrome and WebKit so we encourage you to check your site.

## Summary of Changes

### `hasOwnProprery` on a DOM Object instance will now return `false`

Chrome 42 and earlier 

{% highlight javascript %}
> div = document.createElement("div");
> div.hasOwnProperty("id");

true
{% endhighlight %}

Chrome 43 onwards

{% highlight javascript %}
> div = document.createElement("div");
> div.hasOwnProperty("id");

false
{% endhighlight %}

### `hasOwnProprery` on a DOM Object instance prototype will now return `true`

Chrome 42 and earlier

{% highlight javascript %}
> div.__proto__.__proto__.hasOwnProperty("id");

false
{% endhighlight %}

Chrome 43 onwards

{% highlight javascript %}
> div.__proto__.__proto__.hasOwnProperty("id");

true
{% endhighlight %}

### Object.getOwnPropertyDescriptor on DOM Object Instance will no longer return a property descriptor for Attributes.

Chrome 42 and earlier

{% highlight javascript %}
> Object.getOwnPropertyDescriptor(div, "id");

Object {value: "", writable: true, enumerable: true, configurable: true}
{% endhighlight %}

Chrome 43 onwards

{% highlight javascript %}
> Object.getOwnPropertyDescriptor(div, "id");

undefined
{% endhighlight %}

### Object.getOwnPropertyDescriptor through the __proto__ on an DOM Object instance will now return a property descriptor 

Chrome 42 and earlier

{% highlight javascript %}
> Object.getOwnPropertyDescriptor(div.__proto__.__proto__, "id");  

undefined
{% endhighlight %}

Chrome 43 onwards

{% highlight javascript %}
> Object.getOwnPropertyDescriptor(div.__proto__.__proto__, "id");

Object {get: function, set: function, enumerable: false, configurable: false}
{% endhighlight %}

### JSON.stringify will no longer serialize DOM Attributes

JSON.stringify doesn’t serialize DOM Attributes on the prototype.  For example, this can affect your site if you are trying to serialize an object such as Push Notification’s [PushSubscription](https://w3c.github.io/push-api/#pushsubscription-interface).

Chrome 42 and earlier

{% highlight javascript %}
> JSON.stringify(subscription);

{
  "endpoint": "https://something",
  "subscriptionId": “SomeID”
}
{% endhighlight %}

Chrome 43 onwards

{% highlight javascript %}
> JSON.stringify(subscription);

{}
{% endhighlight %}


### Writing to read-only properties in strict mode will throw an error

{% highlight javascript %}
function foo() {
  "use strict";
  var d = document.createElement("div");
  d.isContentEditable = 1;
  console.log(d.isContentEditable);
}
{% endhighlight %}

Chrome 42 and earlier

{% highlight javascript %}
> foo();

false // isContentEditable
{% endhighlight %}

Chrome 43 onwards

{% highlight javascript %}
> foo();

Uncaught TypeError: Cannot set property isContentEditable of #<HTMLElement> which has only a getter
{% endhighlight %}




